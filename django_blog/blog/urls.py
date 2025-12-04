from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView,LogoutView
from . import views
from .views import Postlistview,PostCreateView,PostUpdateView,PostDeleteView,Postdetailview
#from .views import register
urlpatterns = [
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/',views.register,name='signup'),
    path('profile/',views.profile,name='profile'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('posts/',Postlistview.as_view(),name='list'),
    path('posts/new/',PostCreateView.as_view(),name='Post'),
    path('posts/<int:pk>/',Postdetailview.as_view(),name='detail_list'),
    path('posts/<int:pk>/edit/',PostUpdateView.as_view(),name='Post'),
    path('posts/<int:pk>/delete/',PostDeleteView.as_view(),name='Post'),
]