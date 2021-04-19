from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User # Not sure that we need it..
from django.conf import settings


class Article(models.Model):
    title = models.CharField(
            max_length = 200,
            validators = [MinLengthValidator(2, "Title must be greater than 2 characters")]
    )
    text = models.TextField()

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

    created_at = models.DateTimeField(auto_now_add = True) 
    #! 'auto_now_add' -
    #! Automatically set the field to now when the object is first created. 
    #! Useful for creation of timestamps.
    updated_at = models.DateTimeField(auto_now = True)
    #! 'auto_now' - 
    #! Automatically set the field to now every time the object is saved. 
    #! Useful for “last-modified” timestamps.
    # https://docs.djangoproject.com/en/3.1/ref/models/fields/#datefield

    # Shows up in the admin list
    def __str__(self):
        return self.title
