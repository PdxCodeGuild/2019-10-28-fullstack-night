from django.urls import path
from . import views

app_name = 'signup4'
urlpatterns = [
    path('signup_page4/', views.signup_page4, name="signup_page4"),
    path('signup_user4/', views.signup_user4, name="signup_user4"),
]