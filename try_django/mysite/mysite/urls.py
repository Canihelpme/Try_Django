"""mysite URL Configuration

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
from django.urls import include, path
#include 쓰기위해서는 include 로 import해주자.

urlpatterns = [
    path('news/', include('news.urls')),
    path('polls/', include('polls.urls')),
    #path를 include를 통해 polls.urls에 있는 모든 path를 추가해줄 수 있도록 설정
    #While making app by django you have to set the path in here to connect every app with this mainsite. 
    path('admin/', admin.site.urls),
]
