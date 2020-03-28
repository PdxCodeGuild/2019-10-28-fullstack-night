from django.db import models

class UrlTask(models.Model):
    long_url = models.CharField(max_length=1000000)
    shortened_url = models.CharField(max_length=1000000)
    def __str__(self):
        # console.log(self)
        return f"{self.long_url}{self.shortened_url}"

# Create your models here.
