from django.urls import path
from post import views

app_name = 'post'

urlpatterns = [
    path('', views.index, name='home'),
    path('posts/create/', views.create_post, name='create'),
    path('posts/comments/create/', views.create_comment, name='new_comment'),
    path('posts/likes/like/', views.add_to_likes, name='like'),
    path('posts/likes/dislike/', views.remove_like, name='dislike'),
    path('users/follow/<int:pk>/', views.follow_user, name='follow'),
    path('users/unfollow/<int:pk>/', views.unfollow_user, name='unfollow'),
    path('search/', views.search_user, name='search'),

]
