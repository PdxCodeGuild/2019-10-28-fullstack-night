from django.urls import path

from . import views

app_name = 'calc'

urlpatterns = [
    path('', views.calc, name='calc')
]