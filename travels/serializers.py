from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Travel
# Certifique-se de que este import está correto:
from user.serializers import UserSerializer 

User = get_user_model()

class TravelSerializer(serializers.ModelSerializer):    
    # Sobrescreve o campo para usar o UserSerializer completo (many=True para lista)
    passenger_list = UserSerializer(many=True, read_only=True) 
    
    create_by_name = serializers.ReadOnlyField(source='create_by.get_full_name')
    
    class Meta:
        model = Travel
        fields = ['id', 'start', 'end', 'start_date', 'time', 'places', 'price', 'passenger_list', 'create_by', 'create_by_name', 'created_at', 'updated_at']
        read_only_fields = ['id', 'create_by', 'created_at', 'updated_at', 'create_by_name'] 


class TravelCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travel
        fields = ('start', 'end', 'start_date', 'time', 'places', 'price', 'passenger_list')

    def create(self, validated_data):
        passenger_list_data = validated_data.pop('passenger_list', [])
        validated_data['create_by'] = self.context['request'].user
        
        travel = Travel.objects.create(**validated_data)
        
        if passenger_list_data:
            travel.passenger_list.set(passenger_list_data)
        
        return travel