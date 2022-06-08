from django.shortcuts import render, redirect, HttpResponse
from accounts.forms import SignupForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from post.models import Post
from accounts.models import Profile
from django.contrib.auth.models import User

# Create your views here.


def signup_user(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            created_user = form.save()
            created_user.first_name = full_name.split(' ')[0]
            created_user.last_name = full_name.split(' ')[1]
            created_user.save()
            return redirect('accounts:login')
        form.errors.as_data()
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('post:home')
    return render(request, 'accounts/login.html')


@login_required
def logout_user(request):
    logout(request)
    return redirect('post:home')


@login_required
def user_profile(request, pk):
    users = User.objects.exclude(pk=request.user.pk)
    posts = Post.objects.filter(poster__pk=pk).order_by('-created_at')
    user = Profile.objects.get(user__id=request.user.pk)
    followers = user.followers.all()
    following = user.following.all()
    user_suggestions = users.exclude(
        id__in=following).exclude(id__in=followers)
    return render(request, 'accounts/profile.html', {'posts': posts, 'users': user_suggestions})
