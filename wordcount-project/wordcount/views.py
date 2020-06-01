from django.http import HttpResponse
#for the html file
from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    
    #To split
    words = fulltext.split()
    
    worddictionary={}
    
    for word in words:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word]=1
    
    
    return render(request, 'count.html', {'fulltext':fulltext, 'word':len(words), 'worddictionary': sorted(worddictionary.items())} )

def happy(obj):
    return HttpResponse("<h1>you are too happy today....</h1>")

def about(request):
    return render(request, 'about.html')
    