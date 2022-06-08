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
