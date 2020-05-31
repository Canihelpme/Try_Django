from django.urls import path

from . import views

urlpatterns = [
    path('articles/<int:year>/', views.year_archive, name='year'),
    path('articles/<int:year>/<int:month>/', views.month_archive, name='month'),
]