from rest_framework import serializers
from .models import CustomUser

class userserializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'followers', 'bio', 'profile_picture']