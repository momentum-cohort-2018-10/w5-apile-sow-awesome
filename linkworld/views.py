from django.shortcuts import render, redirect
from linkworld.models import Post, Comment, Vote
from django.shortcuts import get_object_or_404, resolve_url
from linkworld.forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.db.models import Count
from django.contrib import messages


def index(request):
    posts = Post.objects.annotate(vote_counts=Count(
        'votes')).order_by("-vote_counts", "-date")
    comments = Comment.objects.all().order_by("-date")
    return render(request, 'index.html', {'posts': posts, 'comments': comments,
                                          })


def sort_by_date(request):
    posts = Post.objects.order_by("-date")
    return render(request, 'index.html', {'posts': posts,
                                          })


def sort_by_likes(request):
    posts = Post.objects.annotate(vote_counts=Count(
        'votes')).order_by("-vote_counts", "-date")

    return render(request, 'index.html', {'posts': posts,
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
            new_post.author = request.user
            new_post.save()
            messages.success(request, 'Your post is up on the site!')
            return redirect('home')
        else:
            form = PostForm()

        return render(request, 'posts/new_post.html', {'form': form})


@login_required
def delete_new_post(request):
    if request.POST.get('pk'):
        post = get_object_or_404(Post, pk=request.POST.get('pk'))
        if post.author == request.user:
            post.delete()
            messages.success(request, 'Your post has been deleted.')
        else:
            messages.warning(
                request, 'Sorry you are not authorized to delete this post')

        return redirect('home')


@login_required
def comment_on_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.commenter = request.user
            comment.save()
            messages.success(
                request, 'Great, thanks for commenting! Check it out on the post!')
            return redirect('post_detail', slug=post.slug)
        else:
            messages.warning(
                request, 'Sorry something went wrong! Please submit again!')
    else:
        form = CommentForm()
    return render(request, 'posts/comment_on_post.html', {'form': form})


@login_required
def delete_comment(request):

    if request.POST.get('pk'):
        comment = get_object_or_404(Comment, pk=request.POST.get('pk'))
        post = comment.post
        if comment.commenter == request.user:
            comment.delete()
            messages.success(request, 'Your comment has been deleted.')
        else:
            messages.warning(request, 'Sorry you are not authorized to delete this comment'
                             )
    return redirect('post_detail', slug=post.slug)


@login_required
def upvote(request, slug):

    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        if not Vote.objects.filter(post=post, user=request.user):
            Vote.objects.create(post=post, user=request.user)
            messages.success(request, 'Thanks for liking!')
        else:
            messages.info(request, 'You have already liked this post.')
    return redirect(('{}#' + post.slug).format(resolve_url('home')))
