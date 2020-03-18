from django.db import models
from django.contrib.auth.models import User
import random

class UserSecrets(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    user_fear = models.TextField(blank=True)
    user_weak = models.TextField(blank=True)

# Create your models here.
