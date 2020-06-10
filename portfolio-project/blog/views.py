from django.shortcuts import render, get_object_or_404

from .models import Blog
# Create your views here.

def allblogs(req):
    blog = Blog.objects
    return render(req, 'blog/allblogs.html', {'blog':blog})


def detail(req, blog_id):
    detailblog=get_object_or_404(Blog, pk=blog_id)
    return render(req, 'blog/detail.html', {'blog':detailblog})
    
    
