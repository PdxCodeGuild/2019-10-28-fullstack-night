from django.urls import path

from . import views

app_name = 'tracker'

urlpatterns = [
    path('', views.index, name='index'),
    path('meals/', views.meals, name='meals'),
    path('diary-entries/', views.entries, name='diary-entries'),
    path('diary-day/<int:pk>/', views.day, name='day')
]