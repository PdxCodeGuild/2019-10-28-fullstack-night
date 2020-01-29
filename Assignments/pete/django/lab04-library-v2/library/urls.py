from django.urls import path

from . import views

app_name = 'library'

urlpatterns = [
    path('', views.index, name='index'),
    path('checkout-history/<str:title>/', views.checkout_history, name='checkout_history'),
    path('donate/', views.donate, name='donate'),
    path('checkout/<str:title>', views.checkout_book, name='checkout'),
    path('return/<str:title>', views.return_book, name='return'),
    path('choose-author/', views.choose_author, name='choose_author'),
    path('old-author-donate/', views.old_author_donate, name='old_author_donate'),
    path('new-author-donate/', views.new_author_donate, name='new_author_donate'),
]