from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    """vista home"""
    return HttpResponse("<h1>Bienvenidos a mi blog</h1>")
