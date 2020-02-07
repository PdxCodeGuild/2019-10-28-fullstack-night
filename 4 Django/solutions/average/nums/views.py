# nums/views.py
from django.shortcuts import render
from .models import NumberCollection
from django.http import HttpResponseRedirect

def index(request):
    if request.method == 'POST':
        new_collection = NumberCollection(name=request.POST['name'])
        new_collection.save()
        HttpResponseRedirect('/')
    return render(request, 'nums/index.html', {'collections': NumberCollection.objects.all()})

def collection(request, pk):
    active_collection = NumberCollection.objects.get(pk=pk)
    return render(request, 'nums/collection.html', {'collection': active_collection})
