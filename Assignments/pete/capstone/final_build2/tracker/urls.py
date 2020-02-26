from django.urls import path

from . import views

app_name = 'tracker'

urlpatterns = [
    path('', views.tracker, name='tracker'),
    path('add-day/', views.add_day, name='add_day'),
    path('day/<int:pk>/', views.get_day, name='get_day'),
    path('entry/<int:pk>/', views.entry, name='entry'),
    path('add-entry/<int:pk>/', views.add_entry, name='add_entry'),
    path('saved-entry/<int:pk>/', views.saved_entry, name='saved_entry'),
]