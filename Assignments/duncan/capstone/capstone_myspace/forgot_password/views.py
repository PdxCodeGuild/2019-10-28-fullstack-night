from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .models import FakePass
import random

def suggested_passwords(request):
    pass_list = list(FakePass.objects.all())
    chosen_pass = []
    for i in range(3):
        random_index = random.randrange(len(pass_list))
        chosen_pass.append(pass_list.pop(random_index))
    print(chosen_pass)
    return render(request, 'forgot_password/forgot_password.html', {"suggested_passes":chosen_pass})

def login_redirect(request):
    return HttpResponseRedirect(reverse('login:login_page'))


# Create your views here.
