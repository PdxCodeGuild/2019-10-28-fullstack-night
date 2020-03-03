# todo/urls.py
from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.index, name='index'),
    path('vue/', views.index_vue, name='index_vue'),
    path('vuesubmit_cats/', views.vue_submit, name='vue_submit'),
]
