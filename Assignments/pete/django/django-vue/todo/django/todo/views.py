from django.shortcuts import render
from django.http import JsonResponse

from .models import Task

def index(request):
    tasks = Task.objects.all()
    task_list = [{
        'id': task.id,
        'text': task.text,
        'created': task.created,
        'completed': task.completed,
        'completed-bool': task.completed_bool,
    } for task in tasks]
    return JsonResponse({'tasks': task_list})