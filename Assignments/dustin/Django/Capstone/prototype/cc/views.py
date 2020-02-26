from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import ArtPiece, Artist
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

#@login_required
def index(request):
    return render(request, "cc/index.html", {})

def profile(request):
    return render(request, 'cc/profile.html', {})


# Create your views here.