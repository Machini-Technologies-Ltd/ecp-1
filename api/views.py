from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>API home</h1>')

def about(request):
    return HttpResponse('<h1>API about</h1>')