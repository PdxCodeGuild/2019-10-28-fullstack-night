from django.urls import path

from . import views

app_name = 'use'

urlpatterns = [
    path('login/', views.login_form, name='login'),
    path('register/', views.register_form, name='register'),
    path('execute-login/', views.execute_login, name="execute_login"),
    path('execute-register/', views.execute_register, name="execute_register"),
]