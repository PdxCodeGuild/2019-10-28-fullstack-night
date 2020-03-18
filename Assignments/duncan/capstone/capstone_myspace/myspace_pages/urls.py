from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'myspace'
urlpatterns = [
    path('', views.index, name='index'),
    path('myspace_vue/', views.myspace_pages_vue, name='myspace_pages_vue'),
    path('vuesubmit/', views.vue_submit, name='vue_submit'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)