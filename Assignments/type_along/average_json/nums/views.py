from django.shortcuts import render
from django.http import JsonResponse
from .models import Number, NumberCollection

def index(request):
    collections = NumberCollection.objects.all()
    name_list = []
    for collection in collections:
        name_list.append(collection.name)
    return JsonResponse({"collections": collections})

# Create your views here.
