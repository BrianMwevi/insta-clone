# Generated by Django 3.2 on 2022-06-05 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20220604_2338'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='description',
            new_name='captions',
        ),
        migrations.RemoveField(
            model_name='post',
            name='hash_tag',
        ),
    ]