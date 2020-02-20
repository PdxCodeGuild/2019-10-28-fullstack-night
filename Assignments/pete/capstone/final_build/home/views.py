from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

import json

def home(request):
    if request.user.is_authenticated:
        return render(request, 'home/base.html', {'user': True})
    return render(request, 'home/base.html', {'user': False})
    