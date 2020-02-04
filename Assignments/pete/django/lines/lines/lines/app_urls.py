from django.urls import path

from . import views

app_name = 'lines'

urlpatterns = [
    path('', views.lines, name='lines'),
]