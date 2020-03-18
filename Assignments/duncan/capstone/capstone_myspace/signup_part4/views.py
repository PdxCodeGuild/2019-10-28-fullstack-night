from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .models import UserNetflix

def signup_page4(request):
    next_place = request.GET.get('next', reverse('signup5:signup_page5'))
    context = {
        'next': next_place,
    }
    return render(request, 'signup_part4/signup_part4_index.html', context)

def signup_user4(request):
    user_netflix = UserNetflix(
        user_net_pass=request.POST['user_net_pass'],
        user=request.user,
    )
    user_netflix.save()
    return HttpResponseRedirect(reverse('signup5:signup_page5'))

# Create your views here.
