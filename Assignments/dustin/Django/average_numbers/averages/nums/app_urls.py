from django.urls import path
from . import views

app_name = 'nums'
urlpatterns = [
    path('collection/<int:pk>/', views.collection, name='collection'),
    path('', views.index, name='index'),
]