from django.urls import path

from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.index, name='index'),
    path('new-task/', views.new_task, name='new_task'),
    path('complete-task/', views.complete_task, name='complete_task'),
]