# Generated by Django 3.2 on 2022-06-07 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_alter_post_poster'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likepost',
            name='post',
        ),
        migrations.RemoveField(
            model_name='likepost',
            name='user',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='likes',
        ),
        migrations.DeleteModel(
            name='LikeComment',
        ),
        migrations.DeleteModel(
            name='LikePost',
        ),
    ]