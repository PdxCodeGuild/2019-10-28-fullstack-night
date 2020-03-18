from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

def home(request):
    user_bool = False
    if request.user.is_authenticated:
        user_bool = True
        return HttpResponseRedirect(reverse('tracker:get_today'))
    return render(request, 'home/base.html', {'user_bool': user_bool})