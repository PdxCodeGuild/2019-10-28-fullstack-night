from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/m/', views.new_movie, name='new_movie'),
    path('new/t/', views.new_tape, name='new_tape'),
    path('mov/<int:pk>', views.movie_detail, name='movie_detail'),
    
]