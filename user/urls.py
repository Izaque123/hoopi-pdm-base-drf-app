from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user.views import ManageUserView, LogoutView
from user.views import ObtainAuthTokenByEmail
from . import views

router = DefaultRouter()
router.register(r'user', views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)), 
    path('me/', ManageUserView.as_view(), name='me'),
    path('api/login/', ObtainAuthTokenByEmail.as_view(), name='api_login'),
    path('api/logout/', LogoutView.as_view(), name='api_logout'),
]