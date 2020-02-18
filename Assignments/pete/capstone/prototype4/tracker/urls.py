from django.urls import path

from . import views

app_name = 'tracker'

urlpatterns = [
    path('', views.index, name='index'),
    path('new-day-form/', views.new_day_form, name='new_day_form'),
    path('new-day/', views.new_day, name='new_day'),
    path('get-day/<int:pk>/', views.get_day, name='get_day'), #pk for DiaryDay
    path('add-entry-form/<int:pk>', views.add_entry_form, name='add_entry_form'), #pk for DiaryDay
    path('add-new-entry/<int:pk>/', views.add_new_entry, name='add_new_entry'), #pk for DiaryDay
    path('add-saved-entry/<int:pk>/', views.add_saved_entry, name='add_saved_entry'), #pk for DiaryDay
    path('suggestion/<int:pk>/', views.suggestion, name='suggestion'),
    path('add-suggested-entry/<int:pk>/', views.add_suggested_entry, name='add_suggested_entry'),
]