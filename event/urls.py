from django.urls import path
from . import views

urlpatterns = [
    path('', views.CalendarView.as_view(), name='calendar'),
    path('new/', views.create_event, name='event_new'),
    path('edit/<int:pk>/', views.EventEdit.as_view(), name='event_edit'),
    path('<int:event_id>/details/', views.event_details, name='event-detail'),
    path('saveNback/', views.saveNback, name='saveNback'),
]