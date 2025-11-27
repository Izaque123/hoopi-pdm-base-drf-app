from rest_framework import serializers
from django.contrib.auth.models import User, Group
from django.contrib.auth.password_validation import validate_password

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