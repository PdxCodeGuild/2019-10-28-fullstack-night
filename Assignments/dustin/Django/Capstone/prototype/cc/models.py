from django.db import models

class ArtPiece(models.Model):
    name = models.CharField(max_length = 64)
    pub_date = models.DateField(auto_now_add=False)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)
    medium = models.CharField(max_length = 32)
    

class Artist(models.Model):
    name = models.CharField(max_length = 32)
    location = models.CharField(max_length = 64)
    bio = models.CharField(max_length = 3000)
    mediums = models.CharField(max_length = 200)
    misc = models.CharField(max_length = 1000)
    
    
    
# Create your models here.
