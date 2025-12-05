from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView,LogoutView
from . import views
from .views import Postlistview,PostCreateView,PostUpdateView, CommentUpdateView,CommentDeleteView,PostDeleteView,Postdetailview,CommentCreate,CommentCreateView
#from .views import register
urlpatterns = [
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/',views.register,name='signup'),
    path('profile/',views.profile,name='profile'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('post/',Postlistview.as_view(),name='list'),
    path('post/new/',PostCreateView.as_view(),name='Post-create'),
    path('post/<int:pk>/',Postdetailview.as_view(),name='detail_list'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='Post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='Post-delete'),
    path('post/<int:pk>/comments/',CommentCreateView.as_view(),name='Comment_list'),
    path('post/<int:pk>/comments/new/',CommentCreate.as_view(),name='new_comment'),
    path('post/<int:pk>/comments/update/',CommentUpdateView.as_view(),name='comment_update'),
    path('post/<int:pk>/comments/delete/',CommentDeleteView.as_view(),name='comment_delete')
]