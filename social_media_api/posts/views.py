from django.shortcuts import render,get_object_or_404
from .models import Post,Comment
from rest_framework import viewsets, permissions,status,generics
from .serializers import PostSerializer,CommentSerializer
from rest_framework import filters
from django_filters import rest_framework as filterz
from django.contrib.auth import get_user_model

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

        return Post.objects.filter(
            author__in=following_users
            ).order_by('-created_at')