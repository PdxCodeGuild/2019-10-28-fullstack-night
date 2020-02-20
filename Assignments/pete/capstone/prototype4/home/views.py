from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'home/index.html')

@login_required
def home(request):
    return render(request, 'home/home.html', {'user': request.user})

def base(request):
    return render(request, 'home/base.html')