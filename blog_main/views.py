


from django.http import HttpResponse
from django.shortcuts import redirect, render

from assignments.models import About
from .forms import RegistrationForm
from blogs.models import Blog, Category
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth


def home(request):
    featured_blogs=Blog.objects.filter(is_featured=True).order_by('-created_at')
    posts=Blog.objects.filter(status='Published')
    try:
        about=About.objects.get()
    except:
        about=None    

    context={
        'featured_blogs':featured_blogs,
        'posts':posts,
        'about':about,
    }
    return render(request,'home.html',context)



def register(request):

    
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:            
        form=RegistrationForm()
    context={
        'form':form,
    }
    return render(request,'register.html',context)




def login(request):
    if request.method == 'POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')


            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
            return redirect('home')

            

    form=AuthenticationForm()
    context={
        'form':form,
    }

    return render(request,'login.html',context)



def logout(request):
    auth.logout(request)
    return redirect('home')
