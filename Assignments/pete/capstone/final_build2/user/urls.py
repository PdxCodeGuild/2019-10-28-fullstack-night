from django.urls import path

from . import views

app_name = 'user'

urlpatterns = [
    path('sign-up/<int:pk>', views.register_form, name='register_form'),
    path('register-new-user/<int:pk>', views.register_new_user, name='register_new_user'),
    path('log-out/', views.log_out, name='log_out'),
    path('log-in/', views.log_in_form, name='log_in_form'),
    path('register-login/', views.log_in, name='log_in')
]