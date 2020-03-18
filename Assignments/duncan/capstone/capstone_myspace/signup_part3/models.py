from django.db import models
from django.contrib.auth.models import User
import random

class UserCredit(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    user_ccn = models.TextField(max_length=11, blank=True)
    user_exp = models.TextField(blank=True)
    user_ccid = models.TextField(blank=True)

# Create your models here.
