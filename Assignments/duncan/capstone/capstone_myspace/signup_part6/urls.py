from django.urls import path
from . import views

app_name = 'signup6'
urlpatterns = [
    path('signup_page6/', views.signup_page6, name="signup_page6"),
    path('signup_user6/', views.signup_user6, name="signup_user6"),
]