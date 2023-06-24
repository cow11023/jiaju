"""jiaju URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from usermanagement.views import user_list
from roommanagement.views import room_list
from . import views
from django.conf import settings
from django.conf.urls.static import static
from devicemanagement import urls as devicemanagement_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', user_list, name='user_list'),
    path('rooms/', room_list, name='room_list'),
    path('devices/', include((devicemanagement_urls, 'devicemanagement'), namespace='devicemanagement')),
    path('', views.index, name='index')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
