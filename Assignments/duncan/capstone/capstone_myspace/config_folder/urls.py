"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('myspace/', include('myspace_pages.urls')),
    path('admin/', admin.site.urls),
    path('login/', include('login.urls')),
    path('forgot_password/', include('forgot_password.urls')),
    path('signup/', include('sign_up.urls')),
    path('signup2/', include('signup_part2.urls')),
    path('signup3/', include('signup_part3.urls')),
    path('signup4/', include('signup_part4.urls')),
    path('signup5/', include('signup_part5.urls')),
    path('signup6/', include('signup_part6.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)