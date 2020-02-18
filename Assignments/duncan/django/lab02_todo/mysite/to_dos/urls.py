from django.urls import path, include
from . import views

app_name = 'to_dos'

urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/<int:pk>/', views.index, name='index2'),
    path('complete/', views.complete, name='complete'),
]