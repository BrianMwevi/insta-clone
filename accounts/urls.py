from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup_user, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/<int:pk>/', views.user_profile, name='profile'),
]
