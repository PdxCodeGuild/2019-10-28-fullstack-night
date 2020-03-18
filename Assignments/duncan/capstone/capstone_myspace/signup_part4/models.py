from django.db import models
from django.contrib.auth.models import User
import random

class UserNetflix(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    user_net_pass = models.TextField(max_length=11, blank=True)

# Create your models here.
