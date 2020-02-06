from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addeye/', views.add_eye, name='add_eye'),
    path('addnose/', views.add_nose, name='add_nose'),
    path('addmouth/', views.add_mouth, name='add_mouth'),
    # path(),
]