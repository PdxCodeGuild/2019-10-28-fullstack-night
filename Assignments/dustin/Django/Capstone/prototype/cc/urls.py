from django.urls import path, include
from . import views

app_name = 'cc'
urlpatterns = [
    path('', views.index, name='index'),
]