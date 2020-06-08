from django.shortcuts import render

# Create your views here.

def allblogs(req):
    return render(req, 'blog/allblogs.html')
