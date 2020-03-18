from django.urls import path
from . import views

app_name = 'signup5'
urlpatterns = [
    path('signup_page5/', views.signup_page5, name="signup_page5"),
    path('signup_user5/', views.signup_user5, name="signup_user5"),
]