from django.shortcuts import render
from .models import Post,Comment
from rest_framework import viewsets, permissions
from .serializers import PostSerializer,CommentSerializer
from rest_framework import filters
from django_filters import rest_framework as filterz
# Create your views here.
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