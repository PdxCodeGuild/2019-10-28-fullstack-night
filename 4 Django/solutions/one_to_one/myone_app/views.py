from django.shortcuts import render
from django.http import HttpResponse
from .models import Key, Value

def keys(request):
    return render(request, 'myone_app/keys.html', {'keys': Key.objects.all()})

def values(request):
    return render(request, 'myone_app/vals.html', {'values': Value.objects.all()})
# Create your views here.
