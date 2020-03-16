from django.urls import path
from . import views

app_name = 'short'
urlpatterns = [
    path('short/', views.index, name='index'),
    path('code/', views.coder, name='coder'),
    path('success/<short_url>', views.success, name='success')
]