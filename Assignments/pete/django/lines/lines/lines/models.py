from django.db import models

class LineCollection(models.Model):
    name = models.CharField(max_length=140)

class Line(models.Model):
    x0 = models.IntegerField()
    y0 = models.IntegerField()
    x1 = models.IntegerField()
    y1 = models.IntegerField()
    collection = models.ForeignKey(LineCollection, on_delete=models.CASCADE)
