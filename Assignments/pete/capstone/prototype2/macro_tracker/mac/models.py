from django.db import models
from django.contrib.auth.models import User



class Macros(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE, related_name='macros')
    meas_sys = models.BooleanField()#true for imperial false for metric
    weight = models.IntegerField()
    bfp = models.IntegerField()#body fat percentage
    act_lvl = models.FloatField()
    goal = models.BooleanField()#true for fat loss false for muscle gain

    lbm = models.IntegerField()
    bmr = models.IntegerField()
    
    protein = models.IntegerField()

    train_kcal = models.IntegerField()
    train_fat = models.IntegerField()
    train_carb = models.IntegerField()
    
    rest_kcal = models.IntegerField()
    rest_fat = models.IntegerField()
    rest_carb = models.IntegerField()

    def __str__(self):
        return f"Training Day({self.train_kcal}/{self.train_fat}/{self.train_carb}/{self.protein}); Rest Day({self.rest_kcal}/{self.rest_fat}/{self.rest_carb}/{self.protein})"