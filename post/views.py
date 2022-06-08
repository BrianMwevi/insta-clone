from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect, HttpResponse, reverse
from post.models import Post, Comment
from accounts.models import Profile
from post.forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q


@login_required
def index(request):
    users = User.objects.exclude(pk=request.user.pk)
    posts = Post.objects.order_by('-created_at').all()
    user = Profile.objects.get(user__id=request.user.pk)
    followers = user.followers.all()
    following = user.following.all()
    user_suggestions = users.exclude(
        id__in=following).exclude(id__in=followers)
    return render(request, 'index.html', {'posts': posts, 'users': user_suggestions})


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            poster = Profile.objects.get(user__pk=request.user.pk)
            post = form.save(commit=False)
            post.poster = poster
            post.save()
            form.save_m2m()
            return redirect('post:home')
        # TODO: Handle POST form errors properly
    else:
        form = PostForm()
    return render(request, 'posts/create.html', {'form': form})


@login_required
def create_comment(request):
    if request.method == 'POST':
        post_id = request.POST.get('postId')
        raw_comment = request.POST.get('comment')
        if raw_comment and post_id:
            post = Post.objects.get(id=post_id)
            if post:
                comment = Comment.objects.create(
                    comment=raw_comment, post=post, user=request.user)
                post.comments.add(comment)
                return HttpResponse(comment)

        # TODO: Handle COMMENT form errors properly
        return HttpResponseBadRequest("Invalid Data")
    return HttpResponseBadRequest()


@login_required
def add_to_likes(request):
    if request.method == 'POST':
        post_id = request.POST.get('id')
        if post_id is not None:
            post = Post.objects.get(id=post_id)
            post.likes.add(request.user.id)
            return HttpResponse({"post": post})
    return HttpResponseBadRequest()


@login_required
def remove_like(request):
    if request.method == 'POST':
        post_id = request.POST.get('id')
        if post_id is not None:
            post = Post.objects.get(id=post_id)
            post.likes.remove(request.user.id)
            post.save()
            return HttpResponse({"post": post})
    return HttpResponseBadRequest()


@login_required
def follow_user(request, pk):
    to_follow = User.objects.get(pk=pk)
    Profile.objects.get(
        user__pk=request.user.pk).following.add(to_follow)
    to_follow.profile.followers.add(request.user)
    return redirect('post:home')


@login_required
def unfollow_user(request, pk):
    to_unfollow = User.objects.get(pk=pk)
    Profile.objects.get(
        user__pk=request.user.pk).following.remove(to_unfollow)
    to_unfollow.profile.followers.remove(request.user)
    return redirect(reverse('accounts:profile', kwargs={'pk': request.user.pk}))
