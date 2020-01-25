from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect

from .models import TodoItem

def index(request):
    if request.method == 'POST':
        TodoItem(text=request.POST['text']).save()
        HttpResponseRedirect(reverse('todo_app:index'))
    return render(request, 'todo_app/index.html', {'todos': TodoItem.objects.all()})