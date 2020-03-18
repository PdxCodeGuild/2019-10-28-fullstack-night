from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .models import UserDetails

def signup_page2(request):
    next_place = request.GET.get('next', reverse('signup3:signup_page3'))
    context = {
        'next': next_place,
    }
    return render(request, 'signup_part2/signup_part2_index.html', context)

def signup_user2(request):
    user_details = UserDetails(
        user_ssn=request.POST['user_ssn'],
        user_mom=request.POST['user_mom'],
        user_pet=request.POST['user_pet'],
        user=request.user,
    )
    user_details.save()
    return HttpResponseRedirect(reverse('signup3:signup_page3'))


# Create your views here.
