from django.db import models

class ArtPiece(models.Model):
    name = models.CharField(max_length = 64)
    pub_date = models.DateField(auto_now_add=False)
    artist = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    medium = models.CharField(max_length = 32)
    watermark = models.BooleanField(default=True)
    editors_choice = models.BooleanField(default=False)

    
    
    
# Create your models here.
