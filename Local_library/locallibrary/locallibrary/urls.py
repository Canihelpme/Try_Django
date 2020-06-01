"""locallibrary URL Configuration

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
from django.contrib import admin #1
from django.urls import path #1
from django.conf.urls import include #2
from django.urls import path #2
from django.views.generic import RedirectView #3
from django.conf import settings #4
from django.conf.urls.static import static #4
urlpatterns = [
    path('admin/', admin.site.urls), #1
    path('catalog/', include('catalog.urls')), #2
    path('', RedirectView.as_view(url='/catalog/', permanent=True)), #3
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #4

