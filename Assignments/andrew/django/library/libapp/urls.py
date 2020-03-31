from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('history/<str:title>/', views.history, name='history'),
    path('checkout/<str:title>', views.checkout_book, name='checkout'),
    path('choose-author/', views.choose_author, name='choose_author'),
]
