from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, UserCreateSerializer
from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from user.serializers import EmailAuthTokenSerializer
from rest_framework.settings import api_settings

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

class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,) 

    def get_object(self):
        return self.request.user
    
@extend_schema(tags=['User.Auth'])
class ObtainAuthTokenByEmail(ObtainAuthToken):
    serializer_class = EmailAuthTokenSerializer 
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

# Adicione esta nova classe para Logout
@extend_schema(tags=['User.Auth'])
class LogoutView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        if request.user.auth_token:
            request.user.auth_token.delete()
            return Response({"detail": "Logout successful."}, status=200)
        
        return Response({"detail": "No active session found."}, status=204)