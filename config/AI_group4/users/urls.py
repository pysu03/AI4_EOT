from django.contrib import admin
from django.urls import path, include
from users     import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('registerForm/', views.registerForm, name='registerForm'),
    path('register/', views.register, name='register'),
    path('loginProc/', views.loginProc, name='loginProc'),
    path('recommendForm/', views.recommendForm, name='recommendForm'),
]
