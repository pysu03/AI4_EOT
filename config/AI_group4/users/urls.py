from django.contrib import admin
from django.urls import path, include
from users     import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('registerForm/', views.registerForm, name='registerForm'),
    path('register/', views.register, name='register'),
    path('loginProc/', views.loginProc, name='loginProc'),
    path('logout/', views.logout, name='logout'),
    path('loginAuth/', auth_views.LoginView.as_view(template_name='users/loginAuth.html'), name='loginAuth'),

]
