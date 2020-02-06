from django.shortcuts import render
from django.http import HttpResponse

from .models import Author, Post

def index(request):
    return render(request, 'blog/index.html', {'posts': Post.objects.all()})