# Generated by Django 3.2 on 2022-06-04 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20220604_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_comment', to='post.LikeComment'),
        ),
    ]
