from django.urls import path,include
from .views import PostViewSet,CommentViewSet,PostFeed
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'posts',PostViewSet)
router.register(r'comments',CommentViewSet)
router.register(r'feed',PostFeed)

urlpatterns=[
    path('',include(router.urls)),
]