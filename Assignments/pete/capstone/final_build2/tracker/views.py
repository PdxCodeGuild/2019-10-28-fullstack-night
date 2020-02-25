from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import *

@login_required
def tracker(request):
    days = DiaryDay.objects.order_by('-date')
    days_json = [day.date for day in days]
    return render(request, 'tracker/tracker.html', {'days': days, 'days_json': days_json})

@login_required
def add_day(request):
    training = request.POST['day-type'] == 'train'
    date = request.POST['date']
    day = DiaryDay(user=request.user, training=training, date=date)
    day.save()
    return HttpResponseRedirect(reverse('tracker:get_day', kwargs={'pk': day.pk}))
    # return render(request, 'tracker/day.html', {'day': day, 'macros': day.macros()})

@login_required
def get_day(request, pk):
    day = DiaryDay.objects.get(pk=pk)
    totals = day.total()
    offset = day.offset()
    over_under = day.over_under()
    return render(request, 'tracker/day.html', {'day': day, 'macros': day.macros(), 'totals': totals, 'offset': offset, 'over_under': over_under})