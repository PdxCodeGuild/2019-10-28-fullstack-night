from django.db import models

class NumberCollection(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class Number(models.Model):
    number = models.IntegerField()
    numbercollection = models.ForeignKey(NumberCollection, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.number} in {self.numbercollection}"
