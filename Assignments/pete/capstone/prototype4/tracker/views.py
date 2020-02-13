from django.shortcuts import render, reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Meal, DiaryDay, DiaryEntry

@login_required
def index(request):
    return render(request, 'tracker/index.html', {'user': request.user})

@login_required
def new_day_form(request):
    return render(request, 'tracker/new-day-form.html')

@login_required
def new_day(request):
    training = request.POST['day-type'] == 'train'
    date = request.POST['date']
    day = DiaryDay(user=request.user, training=training, date=date)
    day.save()
    return render(request, 'tracker/day.html', {'day': day, 'macros': request.user.macros})

@login_required
def get_day(request, pk):
    day = DiaryDay.objects.get(pk=pk)
    totals = day.total()
    offset = day.offset(day.training)
    return render(request, 'tracker/day.html', {'day': day, 'macros': request.user.macros, 'totals': totals, 'offset': offset})

@login_required
def add_entry_form(request, pk):
    day = DiaryDay.objects.get(pk=pk)
    return render(request, 'tracker/add-entry-form.html', {'day': day})

'''
Next time: I have to make a meal before I can make an entry... so... Fixed this
'''

@login_required
def add_new_entry(request, pk):
    day = DiaryDay.objects.get(pk=pk)
    name = request.POST['name']
    kcal = request.POST['kcal']
    fat = request.POST['fat']
    carb = request.POST['carb']
    protein = request.POST['protein']
    meal = Meal(name=name, kcal=kcal, fat=fat, carb=carb, protein=protein, user=request.user)
    meal.save()
    DiaryEntry(meal=meal, date=day).save()
    totals = day.total()
    offset = day.offset(day.training)
    return render(request, 'tracker/day.html', {'day': day, 'macros': request.user.macros, 'totals': totals, 'offset': offset})

@login_required
def add_saved_entry(request, pk):
    day = DiaryDay.objects.get(pk=pk)
    meal = Meal.objects.get(pk=request.POST['meal'])
    DiaryEntry(meal=meal, date=day).save()
    totals = day.total()
    offset = day.offset(day.training)
    return render(request, 'tracker/day.html', {'day': day, 'macros': request.user.macros, 'totals': totals, 'offset': offset})    