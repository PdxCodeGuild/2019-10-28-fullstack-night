from django.urls import path

from . import views

app_name = 'calc'

urlpatterns = [
    path('', views.calc, name='calc'),
    path('calculate', views.calculate, name='calculate'),
    path('macros/<int:pk>', views.macros, name='macros'),
    path('macros-redirect/', views.macros_redirect, name='macros_redirect'),
]