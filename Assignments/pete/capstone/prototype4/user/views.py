from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
# from django.apps import apps
from calc.models import Macros
from .models import UserProfile #, UserMacros
# from ../mac/models import Macros

def create_account(request, pk):
    macros = Macros.objects.get(pk=pk)
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.create_user(username, email, password)
    macros.user = user
    macros.save()
    login(request, user)
    user_profile = UserProfile(user=User.objects.get(pk=user.pk))
    user_profile.save()
    return HttpResponseRedirect(reverse('home:home'))



def create_account_form(request, pk):
    return render(request, 'user/create-account-form.html', {'macros': Macros.objects.get(pk=pk)})

def login_form(request):
    return render(request, 'user/login-account-form.html')

def login_account(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    login(request, user)
    return HttpResponseRedirect(reverse('home:home'))

def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('home:index'))