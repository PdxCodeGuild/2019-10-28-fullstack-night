from django.db import models

class StrMixin:
    def __str__(self):
        return self.text

class Eye(StrMixin, models.Model):
    text = models.CharField(max_length=1)


class Nose(StrMixin, models.Model):
    text = models.CharField(max_length=1)


class Mouth(StrMixin, models.Model):
    text = models.CharField(max_length=1)



# Create your models here.
