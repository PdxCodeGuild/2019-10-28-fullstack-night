from django.db import models

class Line(models.Model):
    x0 = models.IntegerField()
    y0 = models.IntegerField()
    x1 = models.IntegerField()
    y1 = models.IntegerField()

# Create your models here.
