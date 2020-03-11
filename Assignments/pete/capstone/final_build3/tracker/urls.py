from django.urls import path

from . import views

app_name = 'tracker'

urlpatterns = [
    path('', views.tracker, name='tracker'),

    path('add-day/', views.add_day, name='add_day'),
    path('add-day2/<str:date>/<int:training_bool>/', views.add_day2, name='add_day2'),
    #DON'T FORGET THIS BUTTON BELOW NEEDS TO GO INTO THE TEMPLATE
    path('change-day/<str:date>/', views.change_day, name='change_day'),

    path('day/<int:pk>/', views.get_day, name='get_day'),# change views.get_day <-> views.get_day_charts
    path('day2/<str:date>/', views.get_day2, name='day2'),
    path('day3/<str:date>/', views.get_day3, name='day3'),
    path('day-canvas/<int:pk>/', views.day_canvas, name='day_canvas'),#test for self-made canvas graph in day

    path('entry/<int:pk>/', views.entry, name='entry'),
    path('entry2/<str:date>/', views.entry2, name='entry2'),
    path('entry3/<str:date>/', views.entry3, name='entry3'),

    path('add-entry/<int:pk>/', views.add_entry, name='add_entry'),
    path('saved-entry/<int:pk>/', views.saved_entry, name='saved_entry'),
    path('nutritionix/<int:pk>/', views.nutritionix, name='nutritionix'),
    path('track-custom/<str:date>/', views.track_custom, name='track_custom'),
    path('track-nutritionix/<str:date>/', views.track_nutritionix, name='track_nutritionix'),

    path('calendar/<str:date>/', views.calendar_month, name='calendar'),
    path('calendar-now/', views.calendar_now, name='calendar_now'),
    path('calendar-last/<str:date>/', views.calendar_last, name='calendar_last'),
    path('calendar-next/<str:date>/', views.calendar_next, name='calendar_next'),

    path('day-last/<str:date>/', views.day_last, name='day_last'),
    path('day-next/<str:date>/', views.day_next, name='day_next'),
]