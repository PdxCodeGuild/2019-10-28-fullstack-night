from django.urls import path, include

app_name = 'urlshort'
urlpatterns = [
    path('', views.index, name='index')
]