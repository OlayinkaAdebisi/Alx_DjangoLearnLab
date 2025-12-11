from django.shortcuts import render,get_object_or_404
from .models import CustomUser
from rest_framework import generics,status,permissions
from django.contrib.auth.forms import UserCreationForm
from .serializers import RegisterSerializer,LoginSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType
from posts.models import Post
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

class FollowUserView(generics.GenericAPIView):
    queryset=CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def post(self,request, user_id):
        user_to_follow=get_object_or_404(CustomUser,pk=user_id)

        if user_to_follow==request.user:
            return Response(
                {"error": "You cannot follow yourself"},
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            request.user.following.add(user_to_follow)
            Notification.objects.create(
                recipient=user_to_follow,
                actor=request.user,
                verb='followed you',
                content_type=ContentType.objects.get_for_model(CustomUser),
                object_id=user_to_follow.id
            )
            return Response(
                {"message": f"You are now following {user_to_follow.username}"},
                status=status.HTTP_200_OK
            )
    
    
        
class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()

    def post(self,request, user_id):
        user_to_unfollow=get_object_or_404(CustomUser,pk=user_id)

        if user_to_unfollow==request.user:
            return Response(
                {"error": "You cannot unfollow yourself"},
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            request.user.following.remove(user_to_unfollow)
            return Response(
                {"message": f"You have now unfollowed {user_to_unfollow.username}"},
                status=status.HTTP_200_OK
            )