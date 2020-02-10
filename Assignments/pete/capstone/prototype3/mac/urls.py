from django.urls import path

from . import views

app_name = 'mac'

urlpatterns = [
    path('', views.index, name='index')
]