from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.index, name='index'),
    path('additem/', views.toDoItem),
    path('completeitem/<int:al>/', views.completeItem),
    path('deleteitem/<int:al>/', views.deleteItem),
]