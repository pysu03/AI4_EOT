from django.urls import path, include
# from bulletin.views import boardView
from bulletin   import views

urlpatterns = [
    path('bulletin/', views.bulletin, name='bulletin'),
    path('view/', views.boardView, name='boardView'),
    # path('view/', boardView),
    path('', views.index, name='index'),
    path('write/', views.writePageView, name='writePageView'),
    path('calendar/', views.calendar, name='canlendar'),
]