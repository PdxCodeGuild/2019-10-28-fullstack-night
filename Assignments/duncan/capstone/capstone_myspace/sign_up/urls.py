from django.urls import path
from . import views

app_name = 'signup'
urlpatterns = [
    path('signup_page/', views.signup_page, name='signup_page'),
    path('signup_user/', views.signup_user, name='signup_user'),
]