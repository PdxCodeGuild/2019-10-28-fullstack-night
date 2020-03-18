from django.urls import path
from . import views

app_name = 'forgot_pass'
urlpatterns = [
    path('suggested_passwords/', views.suggested_passwords, name='suggested_passwords'),
    path('login_redirect/', views.login_redirect, name='login_redirect'),
]