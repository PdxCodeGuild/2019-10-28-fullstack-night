from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import ArtPiece
from users.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, "cc/index.html", {})

# @login_required
    # return render(request, 'users/profile.html', {})


# Create your views here.