from django.shortcuts import render
from django.http import HttpResponse

from .models import Meal

def index(request):
    return HttpResponse("hey")

def meals(request):
    return render(request, 'tracker/meals.html', {'meals': Meal.objects.all()})