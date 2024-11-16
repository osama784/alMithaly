from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Admin, Employee
from . import validators as users_validators

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        write_only=True,
        validators=[users_validators.password_length_validator]
        )
    class Meta:
        model = User
        fields = ['username', 'password']


class AdminSerailzer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Admin
        fields = ["user", "created_at"]
        

    def create(self, validated_data):
        user = validated_data.get('user')
        username = user.get('username')
        password = user.get('password')
        user = User.objects.create_user(
            username=username,
            password=password
        )
        instance = Admin.objects.create(
            user = user,
        ) 

        return instance
    

    def update(self, instance, validated_data):
        instance.user.set_password(validated_data.get("password", instance.user.password))
        instance.user.save()

        instance.user.username = validated_data.get("username", instance.user.username)
        instance.user.save()

        return instance


class EmployeeSerailzer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Admin
        fields = ["user", "created_at"]
        

    def create(self, validated_data):
        user = validated_data.get('user')
        username = user.get('username')
        password = user.get('password')
        user = User.objects.create_user(
            username=username,
            password=password
        )
        instance = Employee.objects.create(
            user = user,
        ) 

        return instance
    
    
    def update(self, instance, validated_data):
        user = validated_data.get('user')
        username = user.get('username', instance.user.username)
        password = user.get('password', instance.user.password)
        instance.user.set_password(password)
        instance.user.save()

        instance.user.username = username
        instance.user.save()
        return instance

