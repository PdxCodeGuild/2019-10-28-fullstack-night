from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    groups = Group.objects.all()
    return render(request, 'nums/index.html', {'groups': groups})

# Create your views here.
