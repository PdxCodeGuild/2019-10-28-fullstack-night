from django.shortcuts import render, reverse
from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

import json

from .models import Task


def index(request):
    tasks = Task.objects.all()
    task_list = [{
        'id': task.id,
        'text': task.text,
        'created': task.created,
        'completed': task.completed,
        'completedBool': task.completed_bool,
    } for task in tasks]
    return JsonResponse({'tasks': task_list})

@csrf_exempt
def new_task(request):
    if request.method == 'POST':
        text = json.loads(request.body)['text']
        Task(text=text).save()
        task_list = get_tasks()
        return JsonResponse({'tasks': task_list})

@csrf_exempt
def complete_task(request):
    if request.method == 'POST':
        pk = json.loads(request.body)['id']
        task = Task.objects.get(id=pk)
        task.completed_bool = True
        task.completed = timezone.now()
        task.save()
        task_list = get_tasks()
        return JsonResponse({'tasks': task_list})


def get_tasks():
    tasks = Task.objects.all()
    task_list = [{
        'id': task.id,
        'text': task.text,
        'created': task.created,
        'completed': task.completed,
        'completedBool': task.completed_bool,
    } for task in tasks]
    return task_list