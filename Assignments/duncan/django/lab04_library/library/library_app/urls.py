from django.urls import path
from . import views

app_name = 'library_app'

urlpatters = [
    path('', views.index, name='index'),
    path('auth/pk/', views.author_detail, name='author_detail'),
]