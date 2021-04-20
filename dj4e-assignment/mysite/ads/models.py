from django.db import models

from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.conf import settings

from PIL import Image

# Create your models here.


class Ad(models.Model) :
    title = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Title must be greater than 2 characters")]
    )
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    text = models.TextField()

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Picture
    picture = models.ImageField(default='ad_pics/default.jpg', upload_to='ad_pics')


    def save(self, *args, **kwargs):
        super(Ad, self).save(*args, **kwargs)

        # ReScale the Uploaded Image:
        picture = Image.open(self.picture.path) ## GCP Error
        #image = Image.open(self.picture.name) ## GCP Error
        if(picture.height > 300 or picture.width > 300):
            output_size = (300, 300)
            picture.thumbnail(output_size) # resize the image

            picture.save(self.picture.path)  ## GCP Error
            #image.save(self.image.name)  ## GCP Error


    # Shows up in the admin list
    def __str__(self):
        return self.title



class Comment(models.Model) :
    text = models.TextField(
        validators=[MinLengthValidator(3, "Comment must be greater than 3 characters")]
    )

    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Shows up in the admin list
    def __str__(self):
        if len(self.text) < 15 : return self.text
        return self.text[:11] + ' ...'


class Fav(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('ad', 'user')

    def __str__(self):
        return f'({self.id}) {self.user.username} likes {self.ad.title[:10]}'