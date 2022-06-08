from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.dispatch import receiver
from accounts.models import Profile


class Post(models.Model):
    poster = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    image = CloudinaryField('image')
    captions = models.TextField(blank=False, null=False)
    comments = models.ManyToManyField(
        'Comment', related_name='user_post', blank=True)
    likes = models.ManyToManyField(
        User, related_name='likes', blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.captions


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment = models.CharField(max_length=255, blank=False, null=False)
    post = models.ForeignKey(
        Post, blank=False, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
