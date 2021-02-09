from django.urls import path
from . import views

urlpatterns = [
    path('', views.CalendarView.as_view(), name='calendar'),
    path('new/', views.create_event, name='event_new'),
    path('edit/<int:pk>/', views.EventEdit.as_view(), name='event_edit'),
    path('<int:event_id>/details/', views.event_details, name='event-detail'),
    # path('add_eventmember/<int:event_id>', views.add_eventmember, name='add_eventmember'),
    # path('event/<int:pk>/remove', views.EventMemberDeleteView.as_view(), name="remove_event"),
]