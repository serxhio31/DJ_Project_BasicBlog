from django.shortcuts import render
from .models import Post


# Create your views here.

def index(request):
    return render(request, 'index.html')


def post(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})


def postview(request, pk):
    posts = Post.objects.get(id=pk)
    return render(request, 'postview.html', {'posts': posts})
