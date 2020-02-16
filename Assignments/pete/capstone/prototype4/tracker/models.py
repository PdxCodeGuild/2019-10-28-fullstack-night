from django.db import models
from django.contrib.auth.models import User
from user.models import UserProfile

class Meal(models.Model):
    name = models.CharField(max_length=140)#name of food
    kcal = models.IntegerField()#kilocalories
    fat = models.IntegerField()#g of fat
    carb = models.IntegerField()#g of carb
    protein = models.IntegerField()#g of protein
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meal')
    user = models.ManyToManyField(User, related_name='meal')
    general = models.BooleanField(default=False)#boolean as to whether a meal is available to all users
    def __str__(self):
        return f"{self.name} ({self.kcal}/{self.fat}/{self.carb}/{self.protein})"

class DiaryDay(models.Model):
    date = models.DateField()#date of each diary
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='diary_day')
    training = models.BooleanField()#true for training day false for rest day

    def total(self):
        total_dict = {'kcal': 0, 'fat': 0, 'carb': 0, 'protein': 0}
        for entry in self.diary_entry.all():
            for key in total_dict.keys():
                total_dict[key] += getattr(entry.meal, key)
        return total_dict
    
    def offset(self, training_bool):
        total_dict = self.total()

        if training_bool:
            macros_dict = {
                'kcal': self.user.macros.train_kcal,
                'fat': self.user.macros.train_fat,
                'carb': self.user.macros.train_carb,
                'protein': self.user.macros.protein
            }

        else:
            macros_dict = {
                'kcal': self.user.macros.rest_kcal,
                'fat': self.user.macros.rest_fat,
                'carb': self.user.macros.rest_carb,
                'protein': self.user.macros.protein
            }

        offset_dict = {}
        for key in total_dict.keys():
            offset_dict[key] = total_dict[key] - macros_dict[key]
        return offset_dict

    def over_under(self, training_bool):
        total_dict = self.total()

        if training_bool:
            macros_dict = {
                'kcal': self.user.macros.train_kcal,
                'fat': self.user.macros.train_fat,
                'carb': self.user.macros.train_carb,
                'protein': self.user.macros.protein
            }

        else:
            macros_dict = {
                'kcal': self.user.macros.rest_kcal,
                'fat': self.user.macros.rest_fat,
                'carb': self.user.macros.rest_carb,
                'protein': self.user.macros.protein
            }

        
        over_under_dict = {}
        for key in total_dict.keys():
            if total_dict[key] > macros_dict[key] * 1.1:
                over_under_dict[key] = 'Over'
            elif total_dict[key] < macros_dict[key] * 0.9:
                over_under_dict[key] = 'Under'
            else:
                over_under_dict[key] = 'in Goal Range'
        return over_under_dict


    def __str__(self):
        return str(self.date)

class DiaryEntry(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.PROTECT, related_name='diary_entry')#each entry is linked to a saved meal
    date = models.ForeignKey(DiaryDay, on_delete=models.PROTECT, related_name='diary_entry')
    time = models.TimeField(auto_now=True)#the time of the entry
    #add ForeignKey to user soon
    def __str__(self):
        return f"{self.date} {self.time} {self.meal}"
