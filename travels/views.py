from rest_framework import viewsets, permissions, generics, authentication
from .models import Travel
from .serializers import TravelSerializer, TravelCreateSerializer
from drf_spectacular.utils import (
    extend_schema,
)
from django.db.models import Q # Importamos Q para combinar filtros

# Create your views here.

@extend_schema(tags=['Travel.Views'])
class TravelViewSet(viewsets.ModelViewSet):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,) 

    # Mantemos o queryset original para que as outras ações do ModelViewSet funcionem
    queryset = Travel.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return TravelCreateSerializer
        return TravelSerializer


@extend_schema(tags=['Travel.Views'])
class UserTravelsByDateView(generics.ListAPIView):
    """
    Retorna a lista de viagens de um usuário para uma data específica (opcional).
    Filtra por:
    1. Usuário logado (criador ou passageiro).
    2. Parâmetro de query 'date' (start_date).
    """
    serializer_class = TravelSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        
        # Filtro base: Viagens criadas OU onde o usuário é passageiro
        queryset = Travel.objects.filter(
            Q(create_by=user)
        ).distinct()
        
        # Filtro Adicional: Filtrar pela data (start_date) se fornecida
        date_param = self.request.query_params.get('date')
        
        if date_param:
            queryset = queryset.filter(start_date=date_param)
            
        return queryset.order_by('start_date', 'time')