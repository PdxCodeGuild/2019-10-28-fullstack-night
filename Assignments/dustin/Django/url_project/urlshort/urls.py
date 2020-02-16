from django.urls import path, include
from . import views

app_name = 'urlshort'

urlpatterns = [
    path('', views.index, name='index'),
    path('link/<str:user_url>/', views.redir, name='code')
]