# Generated by Django 3.2 on 2022-06-04 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comments',
            field=models.ManyToManyField(null=True, related_name='user_post', to='post.Comment'),
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(null=True, related_name='liked_post', to='post.LikePost'),
        ),
    ]
