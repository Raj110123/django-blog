


from django.http import HttpResponse
from django.shortcuts import render

from assignments.models import About
from blogs.models import Blog, Category


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