from rest_framework import serializers
from .models import Post,Comment
from django.contrib.auth import get_user_model

User = get_user_model
class PostSerializer(serializers.ModelSerializer):
    author_name=serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Post
        fields = ['id','author','author_name','title','content','created_at','updated_at']

        read_only_fields=['author_name']

class CommentSerializer(serializers.ModelSerializer):
    user_name=serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Comment
        fields = "__all__"

        read_only_fields=['user_name']