
from django.contrib import admin
from django.urls import path, include
from users       import views

urlpatterns = [
    path('index/',  views.index,    name='index'),
<<<<<<< Updated upstream
    path('front/',  views.front,    name='front'),
    path('signup/', views.signup,   name='signup'),
    path('login/',  views.login,    name='login'),
    path('signup/', views.signup,   name='signup'),
    path('logout/', views.logout,   name='logout'),
=======
    path('signup/', views.signup,   name='signup'),
    path('login/',  views.login,    name='login'),
    path('logout/', views.logout,   name='logout'),
    path('weather/',views.weather,  name='weather'),
>>>>>>> Stashed changes

]