from django.shortcuts import render
from .models import CustomUser
from rest_framework import generics
from django.contrib.auth.forms import UserCreationForm
from .serializers import RegisterSerializer,LoginSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
class RegisterView(generics.GenericAPIView):
    serializer_class=RegisterSerializer
    permission_classes = [AllowAny]
    def post(self,request):
        ser=self.get_serializer(data=request.data)
        ser.is_valid(raise_exception=True)
        user = ser.save()
        token, _=Token.objects.get_or_create(user=user)
        return Response({"token":token.key})

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        ser = self.get_serializer(data=request.data)
        ser.is_valid(raise_exception=True)
        user = ser.validated_data
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})