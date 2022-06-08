from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    profile_pic = models.ImageField(
        upload_to='profile/', default="profile/default.png")
    bio = models.TextField(blank=True, null=True)
    followers = models.ManyToManyField(
        User, related_name='followers', blank=True)
    following = models.ManyToManyField(
        User, related_name='following', blank=True)

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()

    def __str__(self):
        return self.user.username
