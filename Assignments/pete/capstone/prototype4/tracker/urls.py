from django.urls import path

from . import views

app_name = 'tracker'

urlpatterns = [
    path('', views.index, name='index'),
    path('new-day-form/', views.new_day_form, name='new_day_form'),
    path('new-day/', views.new_day, name='new_day'),
    path('get-day/<int:pk>/', views.get_day, name='get_day'),
    path('add-entry-form/<int:pk>', views.add_entry_form, name='add_entry_form'),
    path('add-entry/<int:pk>/', views.add_entry, name='add_entry'),
]