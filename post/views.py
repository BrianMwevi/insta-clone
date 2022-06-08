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
        print("form is invalid")
        print(form.errors)
    else:
        form = PostForm()
    return render(request, 'posts/create.html', {'form': form})