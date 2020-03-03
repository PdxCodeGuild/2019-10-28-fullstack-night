from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

def home(request):
    user_bool = False
    if request.user.is_authenticated:
        user_bool = True
    return render(request, 'home/base.html', {'user_bool': user_bool})