from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from .models import Post, Group, User
from django.core.paginator import Paginator


def index(request):
    post_list = Post.objects.select_related('group').order_by('-pub_date')
    paginator = Paginator(post_list,10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'index.html', {'page':page})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    post_list = Post.objects.filter(group=group).order_by('-pub_date')
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'group.html', {'group': group, 'page': page})


@login_required
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'new.html', {'form': form})


def profile(request, username):
    user = User.objects.get(username=username)
    post_list = Post.objects.filter(author=user).order_by('-pub_date')
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    count = Post.objects.filter(author=user).count()
    return render(request, 'profile.html', {'user':user, 'page': page, 'count':count})


def post_view(request, username, post_id):
    user = User.objects.get(username=username)
    count = Post.objects.filter(author=user).count()
    post = Post.objects.get(id=post_id)
    return render(request, 'post.html', {'user':user, 'count':count, 'post':post})


def post_edit(request, username, post_id):
    author = get_object_or_404(User, username=username)
    post = get_object_or_404(Post, id=post_id, author=author)
    login_author = request.user
    if login_author != author:
        return redirect('post', username=author.username, post_id=post.id)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        post.save()
        return redirect('post', username=request.user.username, post_id=post.id)
    return render(request, 'post_edit.html', {'form': form, 'post': post})