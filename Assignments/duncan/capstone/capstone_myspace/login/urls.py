from django.urls import path
from . import views

app_name = 'login'
urlpatterns = [
    path('login_user/', views.login_user, name='login_user'),
    path('login_page/', views.login_page, name='login_page'),
    path('signup_redirect/', views.signup_redirect, name='signup_redirect'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('forgot_pass_redirect/', views.forgot_pass_redirect, name='forgot_pass_redirect'),

    # path('signup_page/', views.signup_user, name='signup_user'),
    # path('signup_user/', views.signup_user, name='signup_user'),
    # path('login_user/', views.login_user, name='login_user'),
]