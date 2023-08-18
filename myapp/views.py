from django.shortcuts import render, redirect
from . models import *
from .forms import PostForm
# Create your views here.

def index(request):
    all_posts = Post.objects.all()
    context = {
        'all_posts':all_posts
    }
    return render(request, 'pages/index.html', context)


def createPost(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('indexPage')
    context = {
        'form':form,
        }
    return render(request, 'post/create.html', context)