from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import AddedItem
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.template import loader

def index(request):
    template = loader.get_template('todo/index.html')
    context = {"al": AddedItem.objects.filter(bool_complete=False), "al2": AddedItem.objects.filter(bool_complete=True)}
    print(context)
    return HttpResponse(template.render(context, request))

def toDoItem(request):
    data = request.POST
    newestItem = AddedItem(new_value=data['item'])
    newestItem.save()
    return HttpResponseRedirect('/')

def completeItem(request, al):
    completedItem = AddedItem.objects.get(pk=al)
    completedItem.bool_complete = True
    print(completedItem.bool_complete)
    completedItem.save()
    return  HttpResponseRedirect('/')

def deleteItem(request, al):
    itemToDelete = AddedItem.objects.get(pk=al)
    itemToDelete.delete()
    return  HttpResponseRedirect('/')



# Create your views here.
