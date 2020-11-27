from rest_framework import serializers
from .models import Employee
from rest_framework.authtoken.models import Token
from django.contrib.auth import password_validation
from django.contrib.auth.models import BaseUserManager


class EmployeeLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True, write_only=True)


class AuthSerializer(serializers.ModelSerializer):
    # auth_token = serializers.SerializerMethodField()

    class Meta:
         model = Employee
         fields = ('id', 'email', 'name', 'is_active', 'role', 'workspace', 'designation', 'phone_number', 'github_username', 'slack_username', 'slack_user_id')
         read_only_fields = ('id', 'is_active', 'is_staff')
    
    def get_auth_token(self, obj):
        token = Token.objects.create(user=obj)
        return token.key


class EmptySerializer(serializers.Serializer):
    pass


class EmployeeRegisterSerializer(serializers.ModelSerializer):
    """
    A user serializer for registering the user
    """

    class Meta:
        model = Employee
        fields = ('id', 'email', 'password', 'name', 'role', 'designation', 'phone_number', 'github_username', 'slack_username', 'slack_user_id')

    def validate_email(self, value):
        # user = Employee.objects.filter(email=value)
        # if user:
        #     return user[0].email
        return BaseUserManager.normalize_email(value)

    def validate_password(self, value):
        password_validation.validate_password(value)
        return value


class PasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_current_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError('Current password does not match')
        return value

    def validate_new_password(self, value):
        password_validation.validate_password(value)
        return value