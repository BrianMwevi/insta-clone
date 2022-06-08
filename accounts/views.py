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
