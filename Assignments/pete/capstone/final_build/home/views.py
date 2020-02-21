from django.shortcuts import render, reverse
from django.http import HttpResponse
from django.contrib.auth.models import User

import json

def home(request):
    user_bool = False
    if request.user.is_authenticated:
        user_bool = True
    context = {
        'user_bool': user_bool,
        'get_started': reverse('calc:home'),
    }

    return render(request, 'home/base.html', context)
    
# def calc(request):
#     return HttpResponse('hi')