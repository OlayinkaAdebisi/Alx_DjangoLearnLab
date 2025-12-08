from django.shortcuts import render
from .models import CustomUser
from rest_framework import generics
from django.contrib.auth.forms import UserCreationForm
from .serializers import userserializer

class APIlist(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class=userserializer

