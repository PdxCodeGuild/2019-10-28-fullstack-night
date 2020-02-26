from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length = 32)
    genre = models.ManyToManyField('Genre')
    rental_price_cents = models.IntegerField()
    image = models.ImageField(upload_to='pics/', null=True, blank=True)

    def __str__(self):
        return self.title
    
    
class Tape(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    condition = models.ForeignKey('Condition', on_delete=models.PROTECT)

    def __str__(self):
        return self.movie.title

class Condition(models.Model):
    # lookup table
    text = models.CharField(max_length = 8)

    def __str__(self):
        return self.text
    
class Genre(models.Model):
    # lookup table
    text = models.CharField(max_length = 16)

    def __str__(self):
        return self.text
    
# Create your models here.
