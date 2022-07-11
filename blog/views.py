from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required

posts =[]
posts=Post.objects.all()

@login_required
def home(request):
    context = {
        'title': 'Home',
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def base(request):
    return render(request, 'blog/base.html')