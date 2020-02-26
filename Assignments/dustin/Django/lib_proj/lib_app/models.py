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

class CheckoutStatus(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE)    
    status = models.BooleanField(default=False)    
    user = models.CharField(max_length = 32)
    time_out = models.TimeField(auto_now_add=True)
    time_in = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.book.title
    


# Create your models here.
