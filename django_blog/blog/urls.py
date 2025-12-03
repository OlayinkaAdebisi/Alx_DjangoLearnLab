from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from . import views
#from .views import register
urlpatterns = [
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/',views.register,name='signup'),
    path('profile/',views.profile,name='profile'),
    path('edit_profile',views.edit_profile,name='edit_profile'),
]