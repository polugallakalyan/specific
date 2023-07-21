from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def first(request):
    return HttpResponse('This is my first string')

def second(request):
    return HttpResponse('<marquee> This is my second string</marquee>')