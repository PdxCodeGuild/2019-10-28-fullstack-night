from django.urls import path

from . import views

app_name = 'library'

urlpatterns = [
    path('', views.index, name='index'),
    path('checkout-history/<str:title>/', views.checkout_history, name='checkout_history'),
    path('donate/', views.donate, name='donate'),
    path('checkout/<str:title>', views.checkout_book, name='checkout'),
    path('return/', views.return_book, name='return'),
]