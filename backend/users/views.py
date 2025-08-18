from django.shortcuts import render
from rest_framework import generics, permissions
from .models import CustomUser
from .serializers import UserRegisterSerializer, UserSerializer, UserTokenSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

# Register user
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegisterSerializer

# Profile view
class ProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

