from django.urls import path
from .views import userlist

urlpatterns = [
    path('user/',userlist.as_view(),name='api_user'),

]