from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 32)
    last_name = models.CharField(max_length = 32)
    phone_number = models.IntegerField()
    

class Address(models.Model):
    user_prof = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    address_num = models.IntegerField()
    street = models.CharField(max_length = 64)
    city = models.CharField(max_length = 32)
    state = models.ForeignKey('State', on_delete=models.PROTECT)
    
    zip_code = models.IntegerField()
    
class State(models.Model):
    # lookup table
    text = models.CharField(max_length = 2)
    
    
    




# Create your models here.
