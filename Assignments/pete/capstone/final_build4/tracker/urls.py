from django.urls import path

from . import views

app_name = 'tracker'

urlpatterns = [
    # TRACKER HOME AND CALENDAR
    path('', views.calendar_now, name='calendar_now'),
    path('calendar-now/', views.calendar_now, name='calendar_now'),
    path('calendar/<str:date>/', views.calendar_month, name='calendar'),
    path('calendar-last/<str:date>/', views.calendar_last, name='calendar_last'),
    path('calendar-next/<str:date>/', views.calendar_next, name='calendar_next'),

    # DAY
    path('add-day/<str:date>/<int:training_bool>/', views.add_day, name='add_day'),
    path('change-day/<str:date>/', views.change_day, name='change_day'),
    path('day/<str:date>/', views.get_day, name='day'),
    path('get-today/', views.get_today, name='get_today'),
    path('day-last/<str:date>/', views.day_last, name='day_last'),
    path('day-next/<str:date>/', views.day_next, name='day_next'),
    
    # ENTRY
    path('entry/<str:date>/', views.entry, name='entry'),
    path('track-custom/<str:date>/', views.track_custom, name='track_custom'),
    path('track-nutritionix/<str:date>/', views.track_nutritionix, name='track_nutritionix'),
    path('track-nutritionix-recipe/<str:date>/', views.track_nutritionix_recipe, name='track_nutritionix_recipe'),
    path('track-saved/<str:date>/', views.track_saved, name='track_saved'),   
]