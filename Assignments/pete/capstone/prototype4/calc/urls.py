from django.urls import path

from . import views

app_name = 'calc'

urlpatterns = [
    path('calc-form/', views.calc_form, name='calc_form'),
    path('calc-macros/', views.calc_macros, name='calc_macros'),
    path('view-macros/', views.view_macros, name='view_macros')
]