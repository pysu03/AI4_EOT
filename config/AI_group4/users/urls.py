from django.urls import path, include
from users       import views


urlpatterns = [
    path('index/',  views.index,    name='index'),
    path('loginForm/', views.loginForm,   name='loginForm'),
    path('accountForm/', views.accountForm,   name='accountForm'),
]