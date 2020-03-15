from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import ArtPiece
from users.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    user = request.user.profile
    banner_image, standard_css, details_css, index_css, submit_css, profile_css = look_select(request)
    css_select = index_css
    banner_image = banner_image
    context = {
        'css_select': css_select,
        'banner_image': banner_image,
        }
    return render(request, "cc/index.html", context)

def details(request):
    user = request.user.profile
    banner_image, standard_css, details_css, index_css, submit_css, profile_css = look_select(request)
    css_select = details_css
    banner_image = banner_image
    associated_works = user.associated_works.objects.all
    context = {
        'css_select': css_select,
        'banner_image': banner_image,
        }
    return render(request, 'cc/details.html', context)

def submitart(request):
    user = request.user.profile
    banner_image, standard_css, details_css, index_css, submit_css, profile_css = look_select(request)
    css_select = submit_css
    banner_image = banner_image
    context = {
        'css_select': css_select,
        'banner_image': banner_image,
        }
    return render(request, 'cc/submitart.html', context)

def textupload(request):
    user = request.user.profile
    
    banner_image, standard_css, details_css, index_css, submit_css, profile_css = look_select(request)
    
    css_select = submit_css
    banner_image = banner_image
    user_select = "textupload"
    context = {
        'css_select': css_select,
        'banner_image': banner_image,
        'user_select': user_select
        }
    return render(request, 'cc/submitart.html', context)

def imageupload(request):
    user = request.user.profile
    
    banner_image, standard_css, details_css, index_css, submit_css, profile_css = look_select(request)
    css_select = submit_css
    banner_image = banner_image
    user_select = "imageupload"
    context = {
        'css_select': css_select,
        'banner_image': banner_image,
        'user_select': user_select,
        }
        
    return render(request, 'cc/submitart.html', context)

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

# @login_required
    # return render(request, 'users/profile.html', {})


# Create your views here.