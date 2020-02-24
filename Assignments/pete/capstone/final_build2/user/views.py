from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

from .models import UserProfile
from calc.models import Macros

def register_form(request, pk):
    return render(request, 'user/register-form.html', {'pk': pk})

def register_new_user(request, pk):
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