from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm

from .models import Post, Group


def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    return render(request, 'index.html', {'posts':posts})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:12]
    return render(request, 'group.html', {'group': group, 'posts': posts})


def new_post(request):
    form = PostForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return HttpResponseRedirect('/')
    return render(request, 'new.html', {'form': form})