from django.db import models

class Meal(models.Model):
    name = models.CharField(max_length=140)#name of food
    kcal = models.IntegerField()#kilocalories
    fat = models.IntegerField()#g of fat
    carbs = models.IntegerField()#g of carbs
    protein = models.IntegerField()#g of protein

class DiaryDay(models.Model):
    date = models.DateField(auto_now=True)#date of each diary

class DiaryEntry(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.PROTECT)#each entry is linked to a saved meal
    date = models.ForeignKey(DiaryDay, on_delete=models.PROTECT)
    time = models.TimeField(auto_now=True)#the time of the entry
