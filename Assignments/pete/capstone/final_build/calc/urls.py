from django.urls import path

from . import views

app_name = 'calc'

urlpatterns = [
    path('', views.home, name='home'),
    path('a/', views.calc_macros, name='calc_macros'),
]