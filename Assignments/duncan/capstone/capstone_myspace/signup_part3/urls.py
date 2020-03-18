from django.urls import path
from . import views

app_name = 'signup3'
urlpatterns = [
    path('signup_page3/', views.signup_page3, name="signup_page3"),
    path('signup_user3/', views.signup_user3, name="signup_user3"),
]