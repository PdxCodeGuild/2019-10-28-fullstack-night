from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("VVelcome to the Library")