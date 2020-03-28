from django.urls import path, include
from . import views

app_name = 'url_short_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('redirect/<str:url_code>', views.redirect_func, name='shortened_url_name'),
    #path('redirect/<int:pk>', views.redirect_func, name='shortened_url_name')
]