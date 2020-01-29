from django.urls import path

from . import views

app_name = 'library'

urlpatterns = [
    path('', views.index, name='index'),
    path('checkout-history/<str:title>/', views.checkout_history, name='checkout_history'),
    path('donate/', views.donate, name='donate'),
    path('checkout/<str:title>', views.checkout_book, name='checkout'),
    path('return/<str:title>', views.return_book, name='return'),
    path('choose-author/<str:author>', views.choose_author, name='choose_author'),
    path('new-author/', views.new_author, name='new_author'),
    path('old-author/<str:author>', views.old_author, name='old_author'),
]