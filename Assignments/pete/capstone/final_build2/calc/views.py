from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

from .models import Macros

def calc(request):
    return render(request, 'calc/calc.html')