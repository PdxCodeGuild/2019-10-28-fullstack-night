from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from myspace_pages.models import UserProfile

def signup_page(request):
    next_place = request.GET.get('next', reverse('signup2:signup_page2')) # Previously: 'myspace:myspace_pages_vue'))
    context = {
        'next': next_place,
    }
    return render(request, 'sign_up/signup_index.html', context)

def signup_user(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.create_user(username, email, password)
    new_profile = UserProfile(user=user)
    new_profile.save()
    new_profile.choose_pic()
    new_profile.save()
    # user.user_profile.choose_pic()
    login(request, user)
    return HttpResponseRedirect(reverse('signup2:signup_page2')) #Previously: 'myspace:myspace_pages_vue'))

# Create your views here.
