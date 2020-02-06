from django.shortcuts import render
from django.http import HttpResponse

from .models import Meal, DiaryDay, DiaryEntry

def index(request):
    return HttpResponse("hey")

def meals(request):
    return render(request, 'tracker/meals.html', {'meals': Meal.objects.all()})

def entries(request):
    return render(request, 'tracker/diary-entries.html', {'entries': DiaryEntry.objects.all()})

def day(request, pk):
    date = DiaryDay.objects.get(pk=pk)
    entries = date.diaryentry_set.all()
    totals = date.total()
    return render(request, 'tracker/day.html', {'entries': entries, 'totals': totals})

