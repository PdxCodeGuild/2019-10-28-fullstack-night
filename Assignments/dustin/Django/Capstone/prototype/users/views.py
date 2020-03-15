from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Profile, Theme, Layout, Medium
from .forms import UserForm, ProfileForm
import os
from django.conf import settings
from django.utils.translation import gettext as _
from itertools import chain

def register_login(request):
    banner_image = "CreativeCrossroadsGIFgreen4.gif"
    css_select = "dark_standard.css"
    next_place = request.GET.get('next', reverse('users:profile'))
    context = {
        'next' : next_place,
        'banner_image': banner_image,
        'css_select': css_select,
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
    user_folder = os.mkdir(os.path.join(settings.MEDIA_ROOT, 'users', username))
    login(request, user)
    return HttpResponseRedirect(reverse('users:profile'))

def logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:register_login'))


# @login_required
def profile(request):
    user = request.user.profile
    
    banner_image, standard_css, details_css, index_css, submit_css, profile_css = look_select(request)
    css_select = profile_css
    banner_image = banner_image

    name = user.name
    bio = user.bio
    location = user.location
    medium = user.mediums
    instagram = f"https://www.instagram.com/{user.instagram}"
    patreon = f"https://www.patreon.com/{user.patreon}"
    soundcloud = f"https://www.soundcloud.com/{user.soundcloud}"
    instagram_username = user.instagram
    patreon_username = user.patreon
    soundcloud_username = user.soundcloud
    # print(instagram)


    context = {
        'css_select': css_select,
        'banner_image': banner_image,
        'bio': bio,
        'name': name, 
        'location': location, 
        'medium': medium,
        'instagram': instagram,
        'patreon': patreon,
        'soundcloud': soundcloud,
        'instagram_username': instagram_username,
        'patreon_username': patreon_username,
        'soundcloud_username': soundcloud_username,
     }
    return render(request, 'users/profile.html', context)


@login_required
def update_profile(request):
    user = request.user.profile
    banner_image, standard_css, details_css, index_css, submit_css, profile_css = look_select(request)
    css_select = standard_css
    banner_image = banner_image
    context = {
        'css_select': css_select,
        'banner_image': banner_image,
        }
    themes = Theme.objects.all()
    layouts = Layout.objects.all()
    mediums = Medium.objects.all()
    

    
    if request.method == 'POST':
        # print(request.POST)
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, files=request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            
        else:
            messages.error(request, _('Please correct the error below.'))
        return HttpResponseRedirect(reverse('users:profile'))
        
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    print(profile_form.__dict__)
    return render(request, 'users/settings.html', dict(chain(profile_form.__dict__.items(), (('css_select', css_select), ('banner_image', banner_image), ('themes', themes), ('layouts', layouts), ('mediums', mediums)))))
    # return render(request, 'users/settings.html', {
    #     'user_form': user_form,
    #     'profile_form': profile_form,
    #     'banner_image': banner_image,
    #     'profile_css': profile_css,
    #     'themes': themes,
    #     'layouts': layouts,
    # })


def look_select(request):
    user = request.user.profile
    if user.theme.text == 'Light':
        banner_image = "CreativeCrossroadsGIFblue.gif"
        standard_css = "light_standard.css"
        details_css = "light_details.css"
        index_css = "light_index.css"
        submit_css = "light_submit.css"
        if user.layout.text == 'Type 1':
            profile_css = "light_profile1.css"
        if user.layout.text == 'Type 2':
            profile_css = "light_profile2.css"
        if user.layout.text == 'Type 3':
            profile_css = "light_profile3.css"
    else:
        banner_image = "CreativeCrossroadsGIFgreen4.gif"
        standard_css = "dark_standard.css"
        details_css = "dark_details.css"
        index_css = "dark_index.css"
        submit_css = "dark_submit.css"
        if user.layout.text == 'Type 2':
            profile_css = "dark_profile2.css"
        if user.layout.text == 'Type 3':
            profile_css = "dark_profile3.css"
        else:
            profile_css = "dark_profile1.css"
    return banner_image, standard_css, details_css, index_css, submit_css, profile_css
        


# Create your views here.
