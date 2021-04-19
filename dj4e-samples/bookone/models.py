from django.db import models


class Lang(models.Model):
    name = models.CharField(max_length = 200)


class Book(models.Model):
    title = models.CharField(max_length = 200)
    isbn = models.CharField(max_length = 13)
    lang = models.ForeignKey('Lang', on_delete = models.SET_NULL, null = True)


class Instance(models.Model):
    book = models.ForeignKey('Book', on_delete = models.CASCADE) 
    # If we will delete the 'Book' entry, this row will be deleted too.
    # CASCADE means that the current row will be deleted too if the ForeignKey gets deleted.
    due_back = models.DateField(null = True, blank = True)
