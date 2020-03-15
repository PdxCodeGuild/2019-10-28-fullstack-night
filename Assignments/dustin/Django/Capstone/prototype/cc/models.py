from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import os

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'users/{0}/{1}'.format(instance.user.username, filename)

class ArtPiece(models.Model):
    name = models.CharField(max_length = 64)
    pub_date = models.DateField(auto_now_add=False)
    artist = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    medium = models.CharField(max_length = 32)
    category = models.CharField(max_length = 150)
    watermark = models.BooleanField(default=True)
    editors_choice = models.BooleanField(default=False)
    image = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
    text = models.TextField()

class ArtCollection(models.Model):
    name = models.CharField(max_length = 64)
    artist = models.ForeignKey('users.Profile', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class CollectionPiece(models.Model):
    collection = models.ForeignKey('ArtCollection', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
    text = models.TextField()

    def __str__(self):
        return str(self.collection)

    
    
    

    
    
    
# Create your models here.
