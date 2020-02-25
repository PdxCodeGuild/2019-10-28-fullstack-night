from django.urls import path

from . import views

app_name = 'tracker'

urlpatterns = [
    path('', views.tracker, name='tracker'),
    path('add-day/', views.add_day, name='add_day'),
    path('day/<int:pk>/', views.get_day, name='get_day'),
]