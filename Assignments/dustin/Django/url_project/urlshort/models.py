from django.db import models

class LinkStart(models.Model):
    url_in = models.CharField(max_length = 5000)
    code = models.CharField(max_length = 9)
    
    
    



# Create your models here.
