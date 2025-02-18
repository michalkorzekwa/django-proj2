from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('event/add/', views.add_event, name='add_event'),
    path('event/<int:event_id>/register/', views.register_event, name='register_event'),
    path('signup/', views.signup, name='signup'),
]