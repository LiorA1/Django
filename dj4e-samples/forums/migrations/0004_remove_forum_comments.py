# Generated by Django 3.1.2 on 2021-03-04 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0003_forum_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forum',
            name='comments',
        ),
    ]
