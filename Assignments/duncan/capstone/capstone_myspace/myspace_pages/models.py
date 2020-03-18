from django.db import models
from django.contrib.auth.models import User
import random

class PostGroup(models.Model):
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)

class ProfilePicChoice(models.Model):
    image = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    # profile pic choice get or create
    # path = 

class ProfileMusicChoice(models.Model):
    music = models.FileField(upload_to='music/', null=True, blank=True)
    def show_song(self):
        return str(self.music).lstrip("music/")

class UserProfile(models.Model):
    profile_pic = models.ForeignKey(
        ProfilePicChoice,
        on_delete=models.PROTECT,
        null = True,
        blank = True,
    )
    profile_music = models.ForeignKey(
        ProfileMusicChoice,
        on_delete=models.PROTECT,
        null = True,
        default = None,
        blank = True,
    )
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    def choose_pic(self):
        self.profile_pic = random.choice(list(ProfilePicChoice.objects.all()))


# random.choice(list(ProfilePicChoice.objects.all()))
# Create your models here.
# user.postgroup_set.all <- this is how you retrieve related information