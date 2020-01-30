from django.urls import path

from . import views

app_name = 'todo_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('complete/', views.complete, name='complete'),
]