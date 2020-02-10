from django.db import models
from django.contrib.auth.models import User
from mac.models import Macros

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_profile')

class UserMacros(Macros):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_macros')