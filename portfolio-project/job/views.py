from django.shortcuts import render

from .models import Job

# Create your views here.


def home(req):
    jobs=Job.objects #To get the data from the Db
    return render(req, 'job/home.html', {'jobs': jobs})
