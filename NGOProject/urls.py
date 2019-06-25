"""NGOProject URL Configuration

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
from django.urls import path, include
from userapp.views import index_view
from adminapp.views import send_email


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', index_view),
    path('', include('django.contrib.auth.urls')),
    path(r'adminapp/', include(('adminapp.urls','adminapp'), namespace='adminapp')),
    # path('signup/', signup_view),
    path(r'userapp/', include(('userapp.urls','userapp'), namespace='userapp')),
    path('index/send_email', send_email),
]
