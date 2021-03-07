from django.db import models

# Create your models here.
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
    created_at = models.DateTimeField(auto_now_add = True) #  ?
    updated_at = models.DateTimeField(auto_now = True)

    # Shows up in the admin list
    def __str__(self):
        return self.title


# Commands -

# from django.db.models import Q, F
# from polls.models import *
# a=Article.objects.filter(created_at__day=F('updated_at__day'))
# a=Article.objects.filter(Q(created_at__day=F('updated_at__day')))