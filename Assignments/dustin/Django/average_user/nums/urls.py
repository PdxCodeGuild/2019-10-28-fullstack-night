from django.urls import path
from . import views

app_name = 'nums'
urlpatterns = [
    path('', views.index, name='index'),
    path('groups/<int:pk>/', views.group, name='group'),
    
]