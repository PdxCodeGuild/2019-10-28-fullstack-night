from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import *

import datetime
import calendar
from dateutil.relativedelta import *

"""
RENDER VIEWS
"""

@login_required
def tracker(request):
    days = DiaryDay.objects.filter(user=request.user).order_by('-date')
    # days = DiaryDay.objects.order_by('-date')
    days_json = [day.date for day in days]
    return render(request, 'tracker/tracker.html', {'days': days, 'days_json': days_json})

@login_required
def get_day(request, pk):
    day = DiaryDay.objects.get(pk=pk)
    totals = day.total()
    offset = day.offset()
    over_under = day.over_under()
    return render(request, 'tracker/day.html', {'day': day, 'macros': day.macros(), 'totals': totals, 'offset': offset, 'over_under': over_under, 'user': request.user})

@login_required
def get_day2(request, date):
    day, created = DiaryDay.objects.get_or_create(date=date, user=request.user, training=True)
    totals = day.total()
    offset = day.offset()
    over_under = day.over_under()
    return render(request, 'tracker/day.html', {'day': day, 'macros': day.macros(), 'totals': totals, 'offset': offset, 'over_under': over_under, 'user': request.user})

    
@login_required
def get_day_charts(request, pk):
    day = DiaryDay.objects.get(pk=pk)
    totals = day.total()
    offset = day.offset()
    over_under = day.over_under()
    return render(request, 'tracker/day-charts.html', {'day': day, 'macros': day.macros(), 'totals': totals, 'offset': offset, 'over_under': over_under, 'user': request.user})
    
@login_required
def entry(request, pk):
    day = DiaryDay.objects.get(pk=pk)
    return render(request, 'tracker/entry.html', {'day': day, 'general_meals': Meal.objects.filter(general=True)})

@login_required
def day_canvas(request, pk):
    day = DiaryDay.objects.get(pk=pk)
    totals = day.total()
    offset = day.offset()
    over_under = day.over_under()
    return render(request, 'tracker/day-canvas.html', {'day': day, 'macros': day.macros(), 'totals': totals, 'offset': offset, 'over_under': over_under, 'user': request.user})
    return HttpResponse('canvas')

@login_required
def nutritionix(request, pk):
    day = DiaryDay.objects.get(pk=pk)
    return render(request, 'tracker/nutritionix.html')

@login_required
def calendar_month(request, date):#date is datetime... just need month and year
    date = datetime.datetime.strptime(date, '%Y-%m-%d')
    month_str = date.strftime('%B')
    month_start, month_length = calendar.monthrange(date.year, date.month)
    year = date.year
    date_str = date.strftime('%Y-%m-%d')
    diary_days = DiaryDay.objects.filter(date__month=date.month, user=request.user)
    logged_days = [day.calendar_dict() for day in diary_days]
    # month_dict = 
    print(diary_days)
    return render(request, 'tracker/calendar.html', {'month_str': month_str, 'year': year, 'date_time': date, 'month_start': month_start, 'month_length': month_length, 'date_str': date_str, 'diary_days': diary_days, 'logged_days': logged_days})

"""
REDIRECT VIEWS
"""
@login_required
def calendar_last(request, date):
    date = datetime.datetime.strptime(date, '%Y-%m-%d')
    last_date = date + relativedelta(months=-1)
    return HttpResponseRedirect(reverse('tracker:calendar', kwargs={'date': last_date.strftime('%Y-%m-%d')}))

@login_required
def calendar_next(request, date):
    date = datetime.datetime.strptime(date, '%Y-%m-%d')
    next_date = date + relativedelta(months=+1)
    return HttpResponseRedirect(reverse('tracker:calendar', kwargs={'date': next_date.strftime('%Y-%m-%d')}))


@login_required
def calendar_now(request):
    today = datetime.date.today()
    return HttpResponseRedirect(reverse('tracker:calendar', kwargs={'date': today}))

@login_required
def add_day(request):
    training = request.POST['day-type'] == 'train'
    date = request.POST['date']
    print('*'*70)
    print(date)
    print('*'*70)
    day = DiaryDay(user=request.user, training=training, date=date)
    day.save()
    return HttpResponseRedirect(reverse('tracker:get_day', kwargs={'pk': day.pk}))
    # return render(request, 'tracker/day.html', {'day': day, 'macros': day.macros()})

@login_required
def add_entry(request, pk):

    day = DiaryDay.objects.get(pk=pk)
    name = request.POST['name']
    kcal = request.POST['kcal']
    fat = request.POST['fat']
    carb = request.POST['carb']
    protein = request.POST['protein']
    meal = Meal(name=name, kcal=kcal, fat=fat, carb=carb, protein=protein)
    meal.save()

    if request.POST.get('save', None):
        meal.user.add(request.user)

    DiaryEntry(meal=meal, date=day).save()
    return HttpResponseRedirect(reverse('tracker:get_day', kwargs={'pk': day.pk}))

@login_required
def saved_entry(request, pk):

    day = DiaryDay.objects.get(pk=pk)
    meal = Meal.objects.get(pk=request.POST['meal'])
    DiaryEntry(meal=meal, date=day).save()
    return HttpResponseRedirect(reverse('tracker:get_day', kwargs={'pk': day.pk}))
