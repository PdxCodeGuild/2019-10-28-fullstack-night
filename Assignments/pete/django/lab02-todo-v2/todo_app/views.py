from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.utils import timezone

from .models import TodoItem

def index(request):
    if request.method == 'POST':
        TodoItem(text=request.POST['text']).save()
        HttpResponseRedirect(reverse('todo_app:index'))
    return render(request, 'todo_app/index.html', {'todos': TodoItem.objects.all()})

def complete(request):
    if request.method == "POST":
        # todos = request.POST.get()
        # for todo in todos:
        #     if todo.pk == int(request.POST['name']):
        #         todo.completed_bool = True
        #         todo.completed_date = timezone.now()
        # todo = TodoItem(pk=request.POST['name'])
        print(request.POST['id'])
        id = request.POST['id']
        todo = TodoItem.objects.get(pk=id)
        todo.completed_bool = True
        todo.completed_date = timezone.now()
        todo.save()
        HttpResponseRedirect(reverse('todo_app:index'))
    return render(request, 'todo_app/index.html', {'todos': TodoItem.objects.all()})