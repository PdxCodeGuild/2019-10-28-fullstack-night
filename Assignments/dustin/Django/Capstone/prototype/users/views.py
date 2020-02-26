from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout


def register_login(request):
    next_place = request.GET.get('next', reverse('cc:index'))
    context = {
        'next' : next_place,
    }
    return render(request, 'users/register_login.html', context)

def register_user(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.create_user(username, email, password)
    login(request, user)
    return HttpResponseRedirect(reverse('cc:index'))

def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    login(request, user)
    return HttpResponseRedirect(reverse('cc:index'))

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:register_login'))



# Create your views here.
