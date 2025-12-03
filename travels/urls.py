from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import UserTravelsByDateView # Importamos a nova View

router = DefaultRouter()
# Mantemos o TravelViewSet para as operações CRUD padrão (create, update, delete)
router.register(r'travel', views.TravelViewSet, basename='travel')

urlpatterns = [
    path('', include(router.urls)), 
    
    # Novo endpoint específico para listagem por data
    path('travels/list_by_date/', UserTravelsByDateView.as_view(), name='travel_list_by_date'),
]