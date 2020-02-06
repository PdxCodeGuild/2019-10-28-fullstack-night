from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name + '!'

class Number(models.Model):
    num = models.IntegerField()
    group = models.ForeignKey('Group', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.num} in {self.group}"

# Create your models here.
