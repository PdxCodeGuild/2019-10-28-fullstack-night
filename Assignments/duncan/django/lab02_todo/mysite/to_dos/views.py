from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from .models import Task

# def task_group(request, pk):
#     new_taskgroup = Task.objects.get(pk=pk)
#     return render(request, 'to_dos/index.html', {'admin_task': Task.objects.filter(chore_status = False), 'admin_task': Task.objects.filter(chore_status = True)})

def index(request):
    if request.method == 'POST':
        new_task = Task(chore_name=request.POST.get('name_chore'))
        new_task.save()
        return HttpResponseRedirect(reverse("to_dos:index"))
    user_tasks = Task.objects.all()
    print(user_tasks)
    return render(request, 'to_dos/index.html', {
        'task_complete': Task.objects.filter(chore_status = True),
        'task_incomplete': Task.objects.filter(chore_status = False),
        })

def complete(request):
    task_pk = (request.POST.get('task'))
    active_task = Task.objects.get(pk=task_pk)
    active_task.chore_status = True
    active_task.save()
    return HttpResponseRedirect(reverse("to_dos:index"))
# Create a Done List!
