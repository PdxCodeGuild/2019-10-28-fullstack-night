from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import os

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'users/{0}/{1}'.format(instance.user.username, filename)

class ArtPiece(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length = 64)
    pub_date = models.DateField(auto_now_add=True)
    artist = models.CharField(max_length = 24)
    medium = models.CharField(max_length = 32)
    category = models.CharField(max_length = 150)
    watermark = models.BooleanField(default=True)
    editors_choice = models.BooleanField(default=False)
    image = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    is_collectionpiece = 0

    def __str__(self):
        return self.name

    def present(self):
        if self.image is not None:
            return self.image.url
        else:
            return "/media/images/Landscape_test.jpg"

class ArtCollection(models.Model):
    name = models.CharField(max_length = 64)
    artist = models.ForeignKey('users.Profile', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class CollectionPiece(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    collection = models.ForeignKey('ArtCollection', on_delete=models.CASCADE)
    pub_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    is_collectionpiece = 1

    def __str__(self):
        return str(self.collection)

    def present(self):
        if self.image is not None:
            return self.image.url
        else:
            return "/media/images/Landscape_test.jpg"

    
    
    

    
    
    
# Create your models here.
