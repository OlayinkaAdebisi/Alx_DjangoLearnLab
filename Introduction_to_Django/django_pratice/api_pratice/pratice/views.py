from django.shortcuts import render
from rest_framework import generics
from .models import user
from .serializers import userserializer
# Create your views here.
class userlist(generics.ListAPIView):
    queryset = user.objects.all()
    serializer_class = userserializer