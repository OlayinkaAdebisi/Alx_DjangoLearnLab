from django.urls import path
from .views import RegisterView, LoginView,FollowUserView,UnfollowUserView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('unfollow/<int:user_id>',UnfollowUserView.as_view()),
    path('follow/<int:user_id>',FollowUserView.as_view())
]
