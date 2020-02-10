from django.urls import path

from . import views

app_name = 'user'

urlpatterns = [
    path('create-account/<int:pk>', views.create_account, name='create_account'),
    path('create-acount-form/<int:pk>', views.create_account_form, name='create_account_form'),
]