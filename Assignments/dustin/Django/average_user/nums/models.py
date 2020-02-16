from django.db import models
from django.contrib.auth.models import User

class Num(models.Model):
    val = models.IntegerField()
    numgroup = models.ForeignKey('NumGroup', on_delete=models.CASCADE, related_name='nums')

class NumGroup(models.Model):
    name = models.CharField(max_length=64)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='numgroups')


# Create your models here.
