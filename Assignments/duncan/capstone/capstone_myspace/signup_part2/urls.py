from django.urls import path
from . import views

app_name = 'signup2'
urlpatterns = [
    path('signup_page2/', views.signup_page2, name="signup_page2"),
    path('signup_user2/', views.signup_user2, name="signup_user2"),
]