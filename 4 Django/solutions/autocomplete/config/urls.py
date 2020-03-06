"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from autocomplete.models import Animal
from django.shortcuts import render
from django.http import JsonResponse
import json

def index(request):
    return render(request, 'autocomplete/index.html', {})

def autocomplete(request):
    data = json.loads(request.body)
    return JsonResponse({'animals': [animal.name for animal in Animal.objects.filter(name__startswith=data['typed'])]})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('autocomplete/', autocomplete, name='autocomplete'),
]
