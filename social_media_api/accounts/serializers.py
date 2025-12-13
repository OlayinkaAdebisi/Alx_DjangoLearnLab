from rest_framework import serializers
from .models import CustomUser
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name','last_name', 'username', 'email', 'password', 'followers']
        read_only_fields = ['followers']
    def create(self, validated_data):
        user = get_user_model().objects.create_user(
        username=validated_data['username'],
        email=validated_data.get('email', ''),
        password=validated_data['password'],
        )
        Token.objects.create(user=user)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password=serializers.CharField()

    def validate(self, attrs):
        user = authenticate(
            username=attrs.get('username'),
            password=attrs.get('password')
        )

        if not user:
            raise serializers.ValidationError("invalid")
        return user