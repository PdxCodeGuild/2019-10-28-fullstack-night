from django.db import models

class ToDo(models.Model):
    text = models.CharField(max_length=128)

    def __str__(self):
        return self.text

# Create your models here.
