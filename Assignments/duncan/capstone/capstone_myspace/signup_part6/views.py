from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .models import UserDob

def signup_page6(request):
    next_place = request.GET.get('next', reverse('myspace:myspace_pages_vue'))
    context = {
        'next': next_place,
    }
    return render(request, 'signup_part6/signup_part6_index.html', context)

def signup_user6(request):
    user_dob = UserDob(
        user_birth=request.POST['user_birth'],
        user=request.user,
    )
    user_dob.save()
    return HttpResponseRedirect(reverse('myspace:myspace_pages_vue'))

# Create your views here.
