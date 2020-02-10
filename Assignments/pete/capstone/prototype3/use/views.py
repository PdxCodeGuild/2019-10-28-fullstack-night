from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

def login_form(request):
    return render(request, 'use/login.html')

def register_form(request):
    return render(request, 'use/register.html')

def execute_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    login(request, user)
    return HttpResponse("You logged in")

def execute_register(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.create_user(username, email, password)
    login(request, user)
    return HttpResponse("You registered")