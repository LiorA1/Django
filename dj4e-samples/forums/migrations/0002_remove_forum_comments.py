# Generated by Django 3.1.2 on 2021-02-08 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forum',
            name='comments',
        ),
    ]