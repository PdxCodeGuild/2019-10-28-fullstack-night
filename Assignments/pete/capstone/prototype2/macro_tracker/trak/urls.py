from django.urls import path

from . import views

app_name = 'trak'

urlpatterns = [
    path('', views.index, name='index'),
    path('diary/', views.diary, name='diary'),
    path('update-diary/', views.update_diary, name='update_diary'),
]