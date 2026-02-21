


from django.http import HttpResponse
from django.shortcuts import render

from blogs.models import Blog, Category


def home(request):
    featured_blogs=Blog.objects.filter(is_featured=True).order_by('-created_at')
    categories=Category.objects.all()
    posts=Blog.objects.filter(status='Published')

    context={
        'featured_blogs':featured_blogs,
        'posts':posts,
    }
    return render(request,'home.html',context)