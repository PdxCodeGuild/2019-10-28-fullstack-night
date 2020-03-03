# todo/views.py
from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import ToDo
from django.http import JsonResponse
import json

def index(request):
    if request.method == 'POST':
        ToDo(
                text=request.POST['text']
                ).save()
        return HttpResponseRedirect(reverse('todo:index'))
    context = {
            'todos': ToDo.objects.all()
            }
    return render(request, 'todo/index.html', context)

def index_vue(request):
    context = {
            'todos': [todo.text for todo in ToDo.objects.all()],
            'submit_to': reverse('todo:vue_submit'),
        }
    return render(request, 'todo/index_vue.html', context)

def vue_submit(request):
    data = json.loads(request.body)
    ToDo(text=data['text']).save()
    context = {
        'todos': [todo.text for todo in ToDo.objects.all()]
    }
    return JsonResponse(context)
