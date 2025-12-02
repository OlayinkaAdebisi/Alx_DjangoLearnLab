from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from . import views
from .views import signup
urlpatterns = [
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/',views.signup,name='signup'),
    path('profile/',views.profile,name='profile'),
]