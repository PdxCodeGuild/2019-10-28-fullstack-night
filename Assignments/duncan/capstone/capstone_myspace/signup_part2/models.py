from django.db import models
from django.contrib.auth.models import User
import random

class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    user_ssn = models.TextField(max_length=11, blank=True)
    user_mom = models.TextField(blank=True)
    user_pet = models.TextField(blank=True)

# Create your models here.
