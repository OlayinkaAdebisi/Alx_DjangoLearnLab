from django.urls import path,include
from .views import PostViewSet,CommentViewSet,PostFeed,LikeView,UnlikeView
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'posts',PostViewSet)
router.register(r'comments',CommentViewSet)
router.register(r'feed/',PostFeed, basename='feed')

urlpatterns=[
    path('',include(router.urls)),
    path('posts/<int:pk>/like/',LikeView.as_view(),name='likes'),
    path('posts/<int:pk>/unlike/',UnlikeView.as_view(),name='unlike')

]