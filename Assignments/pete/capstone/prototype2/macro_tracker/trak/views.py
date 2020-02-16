from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

from .models import Meal, DiaryDay, DiaryEntry

@login_required
def index(request):
    return render(request, 'trak/index.html', {'macros': request.user.macros})

@login_required
def diary(request):
    return render(request, 'trak/diary.html', {'meals': Meal.objects.all()})

@login_required
def update_diary(request):
    if not request.POST['new-day']:
        return HttpResponse('choose day')

    '''
    if request.POST['day-type'] == 'train':
        training = True
    else:
        training = False
    shorter version below
    '''

    training = request.POST['day-type'] == 'train'
    day = DiaryDay(user=request.user, training=training)
    day.save()

    meal = Meal.objects.get(pk=request.POST['meal'])
    entry = DiaryEntry(meal=meal, date=day)
    entry.save()

    entries = day.diary_entry.all()
    totals = day.total()

    return render(request, 'trak/day.html', {'day': day, 'entries': entries, 'totals': totals, 'user': request.user})