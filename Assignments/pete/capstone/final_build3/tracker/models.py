from django.db import models
from django.contrib.auth.models import User
from user.models import UserProfile

class Meal(models.Model):
    name = models.CharField(max_length=140)#name of food
    kcal = models.IntegerField()#kilocalories
    fat = models.IntegerField()#g of fat
    carb = models.IntegerField()#g of carb
    protein = models.IntegerField()#g of protein
    user = models.ManyToManyField(User, related_name='meal')
    general = models.BooleanField(default=False)#boolean as to whether a meal is available to all users
    def __str__(self):
        return f"{self.name} ({self.kcal}/{self.fat}/{self.carb}/{self.protein})"

class DiaryDay(models.Model):
    date = models.DateField()#date of each diary
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='diary_day')
    training = models.BooleanField()#true for training day false for rest day

    def macros(self):
        if self.training:
            return {
                'kcal': self.user.macros.get(active=True).train_kcal,
                'fat': self.user.macros.get(active=True).train_fat,
                'carb': self.user.macros.get(active=True).train_carb,
                'protein': self.user.macros.get(active=True).protein
            }
        return {
            'kcal': self.user.macros.get(active=True).rest_kcal,
            'fat': self.user.macros.get(active=True).rest_fat,
            'carb': self.user.macros.get(active=True).rest_carb,
            'protein': self.user.macros.get(active=True).protein
        }


    def total(self):
        total_dict = {'kcal': 0, 'fat': 0, 'carb': 0, 'protein': 0}
        print(self.diary_entry.all())
        for entry in self.diary_entry.all():
            for key in total_dict.keys():
                    total_dict[key] += getattr(entry.meal, key)
        return total_dict
    
    def offset(self):#removed training_bool
        total_dict = self.total()
        macros_dict = self.macros()

        offset_dict = {}
        for key in total_dict.keys():
            offset_dict[key] = total_dict[key] - macros_dict[key]
        return offset_dict

    def over_under(self):#removed training_bool
        total_dict = self.total()
        macros_dict = self.macros()
        
        over_under_dict = {}
        for key in total_dict.keys():
            if total_dict[key] > macros_dict[key] * 1.1:
                over_under_dict[key] = 'over' #previously: 'Over'
            elif total_dict[key] < macros_dict[key] * 0.9:
                over_under_dict[key] = 'under' #previously: 'Under'
            else:
                over_under_dict[key] = 'goal' #previously: 'in Goal Range'
        return over_under_dict

    def suggestion(self):#removed training_bool
        offset_dict = self.offset()
        over_under_dict = self.over_under()
        
        if over_under_dict['kcal'] != 'Under':
            return None
        
        return Meal.objects.filter(general=True).filter(kcal__lte=(offset_dict['kcal']*-1)).filter(fat__lte=(offset_dict['fat']*-1)).filter(carb__lte=(offset_dict['carb']*-1)).filter(protein__lte=(offset_dict['protein']*-1))

    def sorted(self):
        '''
        Here I want to create a method that sorts by date.
        '''
        pass

    def calendar_dict(self):
        calendar_dict = {
            'train': self.training,
            'year': str(self.date.year),
            'month': str(self.date.month).zfill(2),
            'day': str(self.date.day).zfill(2),
        }
        return calendar_dict

    # def calendar_month_dict(self):
    #     calendar_month_dict = {
    #         'year': str(self.date.year),
    #     }

    def __str__(self):
        return str(self.date)

class DiaryEntry(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.PROTECT, related_name='diary_entry')#each entry is linked to a saved meal
    date = models.ForeignKey(DiaryDay, on_delete=models.PROTECT, related_name='diary_entry')
    time = models.TimeField(auto_now=True)#the time of the entry
    def __str__(self):
        return f"{self.date} {self.time} {self.meal}"
