from django.shortcuts import render
from random import choice
from django.http import HttpResponse, HttpResponseRedirect
from .models import Eye, Nose, Mouth

def get_face_part(in_table):
    results_list = list(in_table.objects.all())
    return str(choice(results_list))

def add_eye(request):
    data = request.POST
    print(data['text'])
    new_eye = Eye(text=data['text'])
    new_eye.save()
    return HttpResponseRedirect('/todo/')

def add_nose(request):
    data = request.POST
    print(data)
    new_nose = Nose(text=data['text'])
    new_nose.save()
    return HttpResponseRedirect('/todo/')

def add_mouth(request):
    data = request.POST
    print(data)
    new_mouth = Mouth(text=data['text'])
    new_mouth.save()
    return HttpResponseRedirect('/todo/')


def index(request):
    emoticon = get_face_part(Eye) + get_face_part(Nose) + get_face_part(Mouth)
    return render(request, 'todoapp/index.html', {'smiley': emoticon})
    
    # Create your views here.
