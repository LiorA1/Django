# Generated by Django 3.1.1 on 2020-11-16 18:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('autos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='comments',
            field=models.CharField(default=django.utils.timezone.now, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='auto',
            name='mileage',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
