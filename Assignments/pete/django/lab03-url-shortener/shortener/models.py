from django.db import models

class Url(models.Model):
    long_url = models.CharField(max_length=140)
    short_url = models.CharField(max_length=14)
    
    def __str__(self):
        return f"{self.pk}\n{self.long_url}\n{self.short_url}\n"