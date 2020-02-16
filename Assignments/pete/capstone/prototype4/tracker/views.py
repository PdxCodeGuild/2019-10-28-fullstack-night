from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
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
    over_under = day.over_under(day.training)
    return render(request, 'tracker/day.html', {'day': day, 'macros': request.user.macros, 'totals': totals, 'offset': offset, 'over_under': over_under})

@login_required
def add_entry_form(request, pk):
    day = DiaryDay.objects.get(pk=pk)
    return render(request, 'tracker/add-entry-form.html', {'day': day, 'general_meals': Meal.objects.filter(general=True)})

'''
Below I learned how to user HttpResponseRedirect() w/ reverse() so compare the commented out functions to the ones below them.
'''

# @login_required
# def add_new_entry(request, pk):
#     day = DiaryDay.objects.get(pk=pk)
#     name = request.POST['name']
#     kcal = request.POST['kcal']
#     fat = request.POST['fat']
#     carb = request.POST['carb']
#     protein = request.POST['protein']
#     meal = Meal(name=name, kcal=kcal, fat=fat, carb=carb, protein=protein, user=request.user)
#     meal.save()
#     DiaryEntry(meal=meal, date=day).save()
#     totals = day.total()
#     offset = day.offset(day.training)
#     over_under = day.over_under(day.training)
#     return render(request, 'tracker/day.html', {'day': day, 'macros': request.user.macros, 'totals': totals, 'offset': offset, 'over_under': over_under})

@login_required
def add_new_entry(request, pk):

    day = DiaryDay.objects.get(pk=pk)
    name = request.POST['name']
    kcal = request.POST['kcal']
    fat = request.POST['fat']
    carb = request.POST['carb']
    protein = request.POST['protein']
    meal = Meal(name=name, kcal=kcal, fat=fat, carb=carb, protein=protein)
    meal.save()
    print('*'*100)
    print(request.POST)
    print(dir(request.POST))
    if request.POST.get('save', None):
        meal.user.add(request.user)

    DiaryEntry(meal=meal, date=day).save()
    return HttpResponseRedirect(reverse('tracker:get_day', kwargs={'pk': day.pk}))

# @login_required
# def add_saved_entry(request, pk):
#     day = DiaryDay.objects.get(pk=pk)
#     meal = Meal.objects.get(pk=request.POST['meal'])
#     DiaryEntry(meal=meal, date=day).save()
#     totals = day.total()
#     offset = day.offset(day.training)
#     over_under = day.over_under(day.training)
#     return render(request, 'tracker/day.html', {'day': day, 'macros': request.user.macros, 'totals': totals, 'offset': offset, 'over_under': over_under})

@login_required
def add_saved_entry(request, pk):
    day = DiaryDay.objects.get(pk=pk)
    meal = Meal.objects.get(pk=request.POST['meal'])
    DiaryEntry(meal=meal, date=day).save()
    return HttpResponseRedirect(reverse('tracker:get_day', kwargs={'pk': day.pk}))