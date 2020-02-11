from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
# from django.apps import apps
from mac.models import Macros
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
    return HttpResponseRedirect(reverse('trak:index'))



def create_account_form(request, pk):
    return render(request, 'user/create-account.html', {'macros': Macros.objects.get(pk=pk)})