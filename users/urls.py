from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.logout, name='logout'),
<<<<<<< HEAD
=======
    path('activate/<str:uidb64>/<str:token>/', views.activate, name="activate"),
>>>>>>> remotes/origin/feature/login/ykk
]
