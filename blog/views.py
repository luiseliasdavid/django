from django.shortcuts import render, HttpResponse
from .models import Post

# Create your views here.


def home(request):
    """vista home"""
    
    posts = Post.objects.all()
    return render(request, "blog/home.html", {"posts":posts})

def post(request,post_id):
    """vista post"""
    
    one_post = Post.objects.get(id=post_id)
    return render(request, "blog/post.html", {"post":one_post})
