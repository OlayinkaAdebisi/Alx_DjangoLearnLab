from rest_framework import serializers
from .models import user, BlogPost, Comment

class userserializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['fullname','last_name','first_name']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content', 'author', 'created_at']

class BlogPostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'author', 'comments', 'created_at']