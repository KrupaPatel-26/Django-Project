from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def Hello_world(request):
    return HttpResponse("Hello,world! This is my fist Django app.")