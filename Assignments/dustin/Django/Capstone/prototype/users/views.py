from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import UserForm, ProfileForm
import os
from django.conf import settings


def register_login(request):
    next_place = request.GET.get('next', reverse('users:profile'))
    context = {
        'next' : next_place,
    }
    return render(request, 'users/register_login.html', context)

def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    login(request, user)
    return HttpResponseRedirect(reverse('users:profile'))

def register_user(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.create_user(username, email, password)
    user_folder = os.mkdir(os.path.join(BASE_DIR, 'users', username))
    login(request, user)
    return HttpResponseRedirect(reverse('users:profile'))

def logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:register_login'))


# @login_required
def profile(request):
    user = request.user.profile
    print(user)
    print(user.theme.text)
    print(user.layout.text)
    #profile_css = "dark_profile1.css"
    if user.theme.text == 'Dark' and user.layout.text == 'Type 1':
        profile_css = "dark_profile1.css"
    if user.theme.text == 'Light' and user.layout.text == 'Type 1':
        profile_css = "light_profile1.css"
    if user.theme.text == 'Dark' and user.layout.text == 'Type 2':
        profile_css = "dark_profile2.css"
    if user.theme.text == 'Light' and user.layout.text == 'Type 2':
        profile_css = "light_profile2.css"
    if user.theme.text == 'Dark' and user.layout.text == 'Type 3':
        profile_css = "dark_profile3.css"
    if user.theme.text == 'Light' and user.layout.text == 'Type 3':
        profile_css = "light_profile3.css"

    name = user.name
    bio = user.bio
    location = user.location
    medium = user.mediums
    instagram = f"https://www.instagram.com/{user.instagram}"
    instagram_username = user.instagram
    # print(instagram)


    context = {
        'profile_css': profile_css,
        'bio': bio,
        'name': name, 
        'location': location, 
        'medium': medium,
        'instagram': instagram,
        'instagram_username': instagram_username
     }
    return render(request, 'users/profile.html', context)


@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return HttpResponseRedirect(reverse('users:update_profile'))
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'users/settings.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


# Create your views here.
