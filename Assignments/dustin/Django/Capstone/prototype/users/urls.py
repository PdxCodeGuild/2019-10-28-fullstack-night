from django.urls import path
from . import views

app_name='users'
urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('register_login/', views.register_login, name='register_login'),
    path('login_user/', views.login_user, name='login_user'),
    path('register_user/', views.register_user, name='register_user'),
    path('logout/', views.logout, name='logout'),
]