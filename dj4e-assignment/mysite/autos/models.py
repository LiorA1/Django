from django.db import models

# Create your models here.


class Make(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        """"""
        return self.name

class Auto(models.Model):
    nickname = models.CharField(max_length=200)
    make = models.ForeignKey(Make, on_delete=models.CASCADE)
    mileage = models.PositiveIntegerField()
    comments = models.CharField(max_length=300)

    def __str__(self):
        """"""
        return self.nickname
