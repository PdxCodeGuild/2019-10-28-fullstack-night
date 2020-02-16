from django.db import models
from django.contrib.auth.models import User
from user.models import UserProfile

class Meal(models.Model):
    name = models.CharField(max_length=140)#name of food
    kcal = models.IntegerField()#kilocalories
    fat = models.IntegerField()#g of fat
    carbs = models.IntegerField()#g of carbs
    protein = models.IntegerField()#g of protein
    def __str__(self):
        return f"{self.name} ({self.kcal}/{self.fat}/{self.carbs}/{self.protein})"

class DiaryDay(models.Model):
    date = models.DateField(auto_now=True)#date of each diary
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='diary_day')
    training = models.BooleanField()#true for training day false for rest day
    def total(self):
        total_dict = {'kcal': 0, 'fat': 0, 'carbs': 0, 'protein': 0}
        for entry in self.diary_entry.all():
            for key in total_dict.keys():
                total_dict[key] += getattr(entry.meal, key)
        return total_dict
    def __str__(self):
        return str(self.date)

class DiaryEntry(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.PROTECT)#each entry is linked to a saved meal
    date = models.ForeignKey(DiaryDay, on_delete=models.PROTECT, related_name='diary_entry')
    time = models.TimeField(auto_now=True)#the time of the entry
    def __str__(self):
        return f"{self.date} {self.time} {self.meal}"
