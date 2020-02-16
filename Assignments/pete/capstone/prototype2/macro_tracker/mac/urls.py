from django.urls import path

from . import views

app_name = 'mac'

urlpatterns = [
    path('', views.index, name='index'),
    path('calc/', views.calc, name='calc'),
    path('calc-macros/', views.calc_macros, name='calc_macros'),
    # path('macros/')
]