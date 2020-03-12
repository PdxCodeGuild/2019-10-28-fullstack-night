"""sokly URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    path('user/', include('django.contrib.auth.urls')),
    # path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  
    path('user/', include('users.urls')),
    path('manager/', TemplateView.as_view(template_name="manager_home.html"), name='manager'),
    path('player_map/', TemplateView.as_view(template_name="player_map.html"), name='player_map'),
    path('roster_page/', TemplateView.as_view(template_name="roster_page.html"), name='roster_page'),
    path('front_page/', TemplateView.as_view(template_name="front_page.html"), name='front_page'),

]


#  added this to enable uploaded file url and it displayed images on html page??
#  this also enables image to be viewable and clickable in api 

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


                              # {% static "path/to/file.css" %}