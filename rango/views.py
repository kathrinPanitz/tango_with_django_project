from django.shortcuts import render

from django.http import HttpResponse

# This is the method for the index
def index(request):
    return HttpResponse("Rango says hey there partner! <br/> <a href='/rango/about/'>About</a>")

# The following code is a new view method called about
def about(request):
    return HttpResponse("Rango says here is the about page. <br/> <a href='/rango/'>Index</a>")
