from django.shortcuts import render,get_object_or_404
from .models import Post,Comment,Like
from rest_framework import viewsets, permissions,status,generics
from .serializers import PostSerializer,CommentSerializer
from rest_framework import filters
from django_filters import rest_framework as filterz
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType
# Create your views here.

User=get_user_model
class ListFilter(filterz.FilterSet):
    class Meta:
        model = Post
        fields = ( 'author', 'title','content')

class PostViewSet(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filterset_class =ListFilter
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['title', 'content']

class CommentViewSet(viewsets.ModelViewSet):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PostFeed(generics.ListAPIView):
    queryset=Post.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        following_users=self.request.following.all()

        return Post.objects.filter(author__in=following_users).order_by('-created_at')
class LikeView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post=generics.get_object_or_404(Post,pk=pk)
        user=self.request.user
        like,created =Like.objects.get_or_create(user=request.user, post=post)

        if created==False:
            return Response(
                            {"message": "You have already liked this post"},
                            status=status.HTTP_400_BAD_REQUEST
                             )
        
        if post.author!=user:
            Notification.objects.create(
                recipient=post.author,
                actor=user,
                verb='liked your post',
                content_type=ContentType.objects.get_for_model(Post),
                object_id=post.id
            )
        return Response(
                        {"message": "You liked this post"},
                             status=status.HTTP_200_OK
                            )

class UnlikeView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request,pk):
        user=self.request.all()
        post=generics.get_object_or_404()
        try:
            like=Like.objects.get(user=request.user,post=post)
            like.delete()
            return Response(
                        {"message": "You unliked this post"},
                             status=status.HTTP_200_OK
                            )
        except Like.DoesNotExist:
            return Response(
                        {"message": "You havent liked this post"},
                             status=status.HTTP_400_BAD_REQUEST
                            )
"""posts/views.py doesn't contain: 
["generics.get_object_or_404(Post, pk=pk)",
 "Like.objects.get_or_create(user=request.user, post=post)",
   "Notification.objects.create"]"""