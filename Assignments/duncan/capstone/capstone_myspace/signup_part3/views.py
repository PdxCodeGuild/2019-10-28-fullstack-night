from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .models import UserCredit

def signup_page3(request):
    next_place = request.GET.get('next', reverse('signup4:signup_page4'))
    context = {
        'next': next_place,
    }
    return render(request, 'signup_part3/signup_part3_index.html', context)

def signup_user3(request):
    user_credit = UserCredit(
        user_ccn=request.POST['user_ccn'],
        user_exp=request.POST['user_exp'],
        user_ccid=request.POST['user_ccid'],
        user=request.user,
    )
    user_credit.save()
    return HttpResponseRedirect(reverse('signup4:signup_page4'))

# Create your views here.
