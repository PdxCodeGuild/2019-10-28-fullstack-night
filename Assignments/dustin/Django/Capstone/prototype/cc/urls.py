from django.urls import path, include
from . import views

app_name = 'cc'
urlpatterns = [
    path('', views.index, name='index'),
    path('details/', views.details, name='details'),
    path('submitart/', views.submitart, name='submitart'),
    path('textupload/', views.textupload, name='textupload'),
    path('imageupload/', views.imageupload, name='imageupload'),
    #path('cc/<str:artist>/<str:artname>/', views.details, name='details'),
]