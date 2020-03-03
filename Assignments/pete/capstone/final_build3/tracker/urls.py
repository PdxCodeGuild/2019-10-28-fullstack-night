from django.urls import path

from . import views

app_name = 'tracker'

urlpatterns = [
    path('', views.tracker, name='tracker'),
    path('add-day/', views.add_day, name='add_day'),
    path('day/<int:pk>/', views.get_day, name='get_day'),# change views.get_day <-> views.get_day_charts
    path('entry/<int:pk>/', views.entry, name='entry'),
    path('add-entry/<int:pk>/', views.add_entry, name='add_entry'),
    path('saved-entry/<int:pk>/', views.saved_entry, name='saved_entry'),
    path('day-canvas/<int:pk>/', views.day_canvas, name='day_canvas'),#test for self-made canvas graph in day
    path('nutritionix/<int:pk>/', views.nutritionix, name='nutritionix'),
    path('calendar/', views.calendar, name='calendar'),
]