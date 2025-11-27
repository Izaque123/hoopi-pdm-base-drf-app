from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, UserCreateSerializer
from drf_spectacular.utils import (
    extend_schema,
)
# Create your views here.

@extend_schema(tags=['User.Views'])

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]

    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        return UserSerializer