from urllib import request
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from blogs.models import Blog, Category

# Create your views here.
def post_by_category(request,category_id):
    posts=Blog.objects.filter(category=category_id,status='Published')
    try:
     category=Category.objects.get(pk=category_id)

    except :
        return redirect("home")

    context={
        'posts': posts,
        'category': category,
    }
    return render(request,'posts_by_category.html',context)