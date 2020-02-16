from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('register_login/', views.register_login, name='register_login'),
    path('register_user/', views.register_user, name='register_user'),
    path('login_user/', views.login_user, name='login_user'),
    path('logout_user/', views.logout_user, name='logout_user'),
]