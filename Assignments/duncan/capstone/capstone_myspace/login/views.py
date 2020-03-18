from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user != None:
        login(request, user)
    else:
        return HttpResponseRedirect(reverse('login:login_page'))
    return HttpResponseRedirect(reverse('myspace:myspace_pages_vue'))

def login_page(request):
    next_place = request.GET.get('next', reverse('myspace:myspace_pages_vue'))
    context = {
        'next': next_place,
    }
    return render(request, 'login/login.html', context)

def signup_redirect(request):
    return HttpResponseRedirect(reverse('signup:signup_page'))

def forgot_pass_redirect(request):
    return HttpResponseRedirect(reverse('forgot_pass:suggested_passwords'))

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('login:login_page'))


# Create your views here.
