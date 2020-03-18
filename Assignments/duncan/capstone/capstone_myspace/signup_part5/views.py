from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .models import UserSecrets

def signup_page5(request):
    next_place = request.GET.get('next', reverse('signup6:signup_page6'))
    context = {
        'next': next_place,
    }
    return render(request, 'signup_part5/signup_part5_index.html', context)

def signup_user5(request):
    user_secrets = UserSecrets(
        user_fear=request.POST['user_fear'],
        user_weak=request.POST['user_weak'],
        user=request.user,
    )
    user_secrets.save()
    return HttpResponseRedirect(reverse('signup6:signup_page6'))

# Create your views here.
