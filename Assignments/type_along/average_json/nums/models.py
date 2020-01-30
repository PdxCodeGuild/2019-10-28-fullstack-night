from django.db import models

class NumberCollection(models.Model):
    name = models.CharField(max_length=64)

class Number(models.Model):
    value = models.IntegerField()
    collection = models.ForeignKey(NumberCollection, on_delete=models.CASCADE)

# Create your models here.
