from django.urls import path
from . import views

urlpatterns = [
    path('', views.weather_detail, name='weather_detail'),
]
