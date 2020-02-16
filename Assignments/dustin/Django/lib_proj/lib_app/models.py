from django.db import models

class Book(models.Model):
    title = models.CharField(max_length = 50)
    year_published = models.IntegerField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    checked_out = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length = 32)
    
    def __str__(self):
        return self.name


# Create your models here.
