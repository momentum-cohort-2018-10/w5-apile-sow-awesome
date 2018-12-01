from django.shortcuts import render, redirect
from linkworld.models import Post, Comment, Vote
from django.shortcuts import get_object_or_404
from linkworld.forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.conf import settings


def index(request):
    posts = Post.objects.all().order_by("-date")
    comments = Comment.objects.all().order_by("-date")
    return render(request, 'index.html', {'posts': posts, 'comments': comments,
                                          })


def post_detail(request, slug):

    post = Post.objects.get(slug=slug)

    return render(request, 'posts/post_detail.html', {
        'post': post,

    })


@login_required
def new_post(request):

    form = PostForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.save()
            return redirect('home')

    else:
        form = PostForm()
    return render(request, 'posts/new_post.html', {'form': form})


@login_required
def delete_new_post(request):
    if request.POST.get('pk'):
        post = get_object_or_404(Post, pk=request.POST.get('pk'))
        post.delete()
        return redirect('home')


@login_required
def comment_on_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            comment.post = post
            comment.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()
    return render(request, 'posts/comment_on_post.html', {'form': form})


@login_required
def delete_comment(request):

    if request.POST.get('pk'):
        comment = get_object_or_404(Comment, pk=request.POST.get('pk'))
        post = comment.post
        comment.delete()
        return redirect('post_detail', slug=post.slug)


@login_required
def upvote(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        if not Vote.objects.filter(post=post, user=request.user):
            Vote.objects.create(post=post, user=request.user)
    return redirect('home')
