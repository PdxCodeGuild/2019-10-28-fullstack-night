from django.urls import path
from . import views

app_name = 'lib'
urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('author_detail/<int:pk>/', views.author_detail, name='author_detail'),
    path('checkout_history/', views.checkout_history, name='checkout_history'),
    path('checkout/<int:pk>/', views.checkout_book, name='checkout'),
]