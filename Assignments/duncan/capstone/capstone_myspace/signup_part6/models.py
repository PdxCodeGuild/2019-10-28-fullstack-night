from django.db import models
from django.contrib.auth.models import User
import random

class UserDob(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    user_birth = models.TextField(blank=True)

# Create your models here.
