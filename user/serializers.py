from rest_framework import serializers
from django.contrib.auth.models import User, Group
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

from django.contrib.auth import authenticate
from rest_framework import serializers

User = get_user_model()

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name']

class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True, read_only=True)
    
    role = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'groups', 'role', 'name']

    def get_role(self, user):
        group = user.groups.first()
        if group:
            return group.name
        return None
    
    def get_name(self, user):
        if user.first_name:
            return f"{user.first_name} {user.last_name}".strip()
        return user.username

class UserCreateSerializer(serializers.ModelSerializer):
    role = serializers.CharField(write_only=True, required=False)
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name', 'role', 'is_active')
        extra_kwargs = {
            'password': {'write_only': True, 'validators': [validate_password]},
        }

    def create(self, validated_data):
        role_name = validated_data.pop('role')

        user = User.objects.create_user(**validated_data)

        try:
            group = Group.objects.get(name=role_name)
            if group.name == 'passenger':
                user.is_staff = False
            else:
                user.is_staff = True

            user.groups.add(group)
                
            user.save()

        except Group.DoesNotExist:
            pass

        return user   

class EmailAuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(label="Email", write_only=True) 
    password = serializers.CharField(
        label="Password",
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(label="Token", read_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'), 
                                username=email, 
                                password=password)
            
        else:
            msg = 'Deve incluir "email" e "password".'
            raise serializers.ValidationError(msg, code='authorization')

        if not user:
            msg = 'Não foi possível fazer o login com as credenciais fornecidas.'
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs