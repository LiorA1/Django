from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.conf import settings


class Thing(models.Model) :
    title = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Title must be greater than 2 characters")]
    )
    text = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)#, related_name='fav_thing_owner')

    #favorites = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Fav', related_name='favorite_things')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Shows up in the admin list
    def __str__(self):
        return f'({self.id}) {self.title}'

# make a boolean field is not much better ? ( No, because different user..)
# 

class Fav(models.Model) :

    thing = models.ForeignKey(Thing, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # https://docs.djangoproject.com/en/3.0/ref/models/options/#unique-together
    class Meta:
        unique_together = ('thing', 'user')

    def __str__(self) :
        return f'({self.id}){self.user.username} likes {self.thing.title[:10]}'
        #return '%s likes %s'%(self.user.username, self.thing.title[:10])
