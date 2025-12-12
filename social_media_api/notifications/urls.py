from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import NotificationListView


urlpatterns=[
    path('notifications/', NotificationListView.as_view(), name='notification-list'),
]