from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('keys', views.keys, name='keys'),
    path('vals', views.values, name='vals'),
]
