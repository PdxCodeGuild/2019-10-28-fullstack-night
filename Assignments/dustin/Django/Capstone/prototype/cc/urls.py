from django.urls import path, include
from . import views

app_name = 'cc'
urlpatterns = [
    path('', views.index, name='index'),
    path('details/<int:pk>/<int:is_collectionpiece>/', views.details, name='details'),
    path('submitart/', views.submitart, name='submitart'),
    path('single_submission/', views.single_submission, name='single_submission'),
    path('collection_submission/', views.collection_submission, name='collection_submission'),
    #path('cc/<str:artist>/<str:artname>/', views.details, name='details'),
]