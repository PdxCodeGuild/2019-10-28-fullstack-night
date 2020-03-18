from django.db import models

class FakePass(models.Model):
    text = models.CharField(max_length=32)
    def __str__(self):
        return self.text


# Create your models here.
