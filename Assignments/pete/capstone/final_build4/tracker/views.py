from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

from .models import *

import datetime
import calendar
from dateutil.relativedelta import *
import json


"""
MONTH
"""

@login_required # TO BE RENAMED "tracker()"?
def calendar_month(request, date):
    date = datetime.datetime.strptime(date, '%Y-%m-%d')
    month_start, month_length = calendar.monthrange(date.year, date.month)
    diary_days = DiaryDay.objects.filter(date__month=date.month, user=request.user)
    diary_days_all = DiaryDay.objects.filter(user=request.user).order_by('-date')

    context = {
        'diary_days_all': diary_days_all,
        'date_time': date,
        'month_str': date.strftime('%B'),
        'year': date.year,
        'month_start': month_start,
        'month_length': month_length,
        'date_str': date.strftime('%Y-%m-%d'),
        'logged_days': [day.calendar_dict() for day in diary_days],
        'day': reverse('tracker:day', kwargs={'date': '$'}),
        'year_month': f"{str(date.year)}-{str(date.month).zfill(2)}-",
    }
    return render(request, 'tracker/calendar.html', context)

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


"""
DAY
"""

@login_required
def get_day(request, date):
    date = datetime.datetime.strptime(date, '%Y-%m-%d')
    date_str = date.strftime("%B %d, %Y")
    date_link = date.strftime('%Y-%m-%d')

    try: 
        day = request.user.diary_day.get(date=date)
        context = {
            'date_str': date_str,
            'date_link': date_link,
            'day': day,
            'macros': day.macros(),
            'totals': day.total(),
            'offset': day.offset(),
            'over_under': day.over_under(),
            'user': request.user,
        }
        return render(request, 'tracker/day.html', context)

    except ObjectDoesNotExist:
        return render(request, 'tracker/day.html', {'date_str': date_str, 'date_link': date_link})

@login_required
def get_today(request):
    today = datetime.date.today()
    return HttpResponseRedirect(reverse('tracker:day', kwargs={'date': today.strftime('%Y-%m-%d')}))

@login_required # TO BE RENAMED "add_day()"
def add_day(request, date, training_bool):
    date = datetime.datetime.strptime(date, '%Y-%m-%d')
    day = DiaryDay(user=request.user, training=training_bool, date=date)
    day.save()
    return HttpResponseRedirect(reverse('tracker:day', kwargs={'date': date.strftime('%Y-%m-%d')}))

@login_required
def change_day(request, date):
    date = datetime.datetime.strptime(date, '%Y-%m-%d')
    day = DiaryDay.objects.get(user=request.user, date=date)
    if day.training:
        day.training = False
    else:
        day.training = True
    day.save()
    return HttpResponseRedirect(reverse('tracker:day', kwargs={'date': date.strftime('%Y-%m-%d')}))

@login_required
def day_last(request, date):
    date = datetime.datetime.strptime(date, '%Y-%m-%d')
    last_date = date + relativedelta(days=-1)
    return HttpResponseRedirect(reverse('tracker:day', kwargs={'date': last_date.strftime('%Y-%m-%d')}))

@login_required
def day_next(request, date):
    date = datetime.datetime.strptime(date, '%Y-%m-%d')
    next_date = date + relativedelta(days=+1)
    return HttpResponseRedirect(reverse('tracker:day', kwargs={'date': next_date.strftime('%Y-%m-%d')}))


"""
ENTRY
"""

@login_required
def entry(request, date):
    date = datetime.datetime.strptime(date, '%Y-%m-%d')

    context = {
        'day': DiaryDay.objects.get(user=request.user, date=date),
        'date_str': date.strftime('%B %d, %Y'),
        'date_link': date.strftime('%Y-%m-%d'),
        'track_custom': reverse('tracker:track_custom', kwargs={'date': '$'}),
        'track_nutritionix': reverse('tracker:track_nutritionix', kwargs={'date': '$'}),
        'track_nutritionix_recipe': reverse('tracker:track_nutritionix_recipe', kwargs={'date': '$'}),
        'day': reverse('tracker:day', kwargs={'date': '$'}),
    }
    return render(request, 'tracker/entry.html', context)

@login_required
def track_custom(request, date):
    date = datetime.datetime.strptime(date, '%Y-%m-%d')
    day = DiaryDay.objects.get(user=request.user, date=date)
    data = json.loads(request.body)

    meal = Meal(
        name=data['name'],
        kcal=data['kcal'],
        fat=data['fat'],
        carb=data['carb'],
        protein=data['protein'],
    )
    meal.save()
    meal.user.add(request.user) #THIS WILL ADD TO SAVED MEALS

    DiaryEntry(meal=meal, date=day).save()
    return HttpResponseRedirect(reverse('tracker:day', kwargs={'date': date.strftime('%Y-%m-%d')}))

@login_required
def track_nutritionix(request, date):
    date = datetime.datetime.strptime(date, '%Y-%m-%d')
    day = DiaryDay.objects.get(user=request.user, date=date)
    data = json.loads(request.body)
    for item in data:
        meal = Meal(
            name=item['name'],
            kcal=item['kcal'],
            fat=item['fat'],
            carb=item['carb'],
            protein=item['protein'],
        )
        meal.save()
        # meal.user.add(request.user) #THIS WILL ADD TO SAVED MEALS

        DiaryEntry(meal=meal, date=day).save()
    return HttpResponse('hey')

@login_required
def track_nutritionix_recipe(request, date):
    date = datetime.datetime.strptime(date, '%Y-%m-%d')
    day = DiaryDay.objects.get(user=request.user, date=date)
    data = json.loads(request.body)
    recipe_dict = {
        'name': f"1/{str(data['portions'])} {data['recipe_name']}",
        'kcal': 0,
        'fat': 0,
        'carb': 0,
        'protein': 0
    }
    for item in data['food_items']:
        recipe_dict['kcal'] += item['kcal'] / data['portions']
        recipe_dict['fat'] += item['fat'] / data['portions']
        recipe_dict['carb'] += item['carb'] / data['portions']
        recipe_dict['protein'] += item['protein'] / data['portions']
    recipe_dict['kcal'] = round(recipe_dict['kcal'])
    recipe_dict['fat'] = round(recipe_dict['fat'])
    recipe_dict['carb'] = round(recipe_dict['carb'])
    recipe_dict['protein'] = round(recipe_dict['protein'])
    meal = Meal(
        name = recipe_dict['name'],
        kcal = recipe_dict['kcal'],
        fat = recipe_dict['fat'],
        carb = recipe_dict['carb'],
        protein = recipe_dict['protein']
    )
    meal.save()
    meal.user.add(request.user)
    DiaryEntry(meal=meal, date=day).save()
    return HttpResponse('hey')

@login_required
def track_saved(request, date):
    date = datetime.datetime.strptime(date, '%Y-%m-%d')
    day = DiaryDay.objects.get(user=request.user, date=date)
    meal = Meal.objects.get(pk=request.POST['meal'])
    DiaryEntry(meal=meal, date=day).save()
    return HttpResponseRedirect(reverse('tracker:day', kwargs={'date': date.strftime('%Y-%m-%d')}))