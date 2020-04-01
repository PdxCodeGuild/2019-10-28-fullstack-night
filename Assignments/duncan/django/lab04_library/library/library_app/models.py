from django.db import models

class Author(models.Model):
    auth_name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    publish = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.PROTECT)



# Create your models here.
