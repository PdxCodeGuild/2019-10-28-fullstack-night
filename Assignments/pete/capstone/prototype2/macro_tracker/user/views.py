from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
# from django.apps import apps
from mac.models import Macros
from .models import UserProfile, UserMacros
# from ../mac/models import Macros

def create_account(request, pk):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.create_user(username, email, password)
    UserProfile(user=User.objects.get(pk=user.pk)).save()
    UserMacros(user_profile=Macros.objects.get(pk=pk)).save()
    login(request, user)
    return render(request, 'trak/index.html')


def create_account_form(request, pk):
    return render(request, 'user/create-account.html', {'macros': Macros.objects.get(pk=pk)})