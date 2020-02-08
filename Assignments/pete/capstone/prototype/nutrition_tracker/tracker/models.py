from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=140)
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
        return self.name

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
    #add training or rest day
    user = models.ForeignKey(UserProfile, on_delete=models.PROTECT)
    training = models.BooleanField(default=True)#true for training day false for rest day
    def total(self):
        total_dict = {'kcal': 0, 'fat': 0, 'carbs': 0, 'protein': 0}
        for entry in self.diaryentry_set.all():
            for key in total_dict.keys():
                total_dict[key] += getattr(entry.meal, key)
        return total_dict
    def __str__(self):
        return str(self.date)

class DiaryEntry(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.PROTECT)#each entry is linked to a saved meal
    date = models.ForeignKey(DiaryDay, on_delete=models.PROTECT)
    time = models.TimeField(auto_now=True)#the time of the entry
    def __str__(self):
        return f"{self.date} {self.time} {self.meal}"
