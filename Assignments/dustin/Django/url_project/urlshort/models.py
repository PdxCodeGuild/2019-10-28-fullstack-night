from django.db import models

class LinkStart(models.Model):
    url_in = models.CharField(max_length=5000)


# Create your models here.
