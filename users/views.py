from django.core.exceptions import ImproperlyConfigured
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import logout

from . import serializers
from .utils import get_and_authenticate_user, create_user_account
from .models import Employee
from workspace.models import Workspace

# Create your views here.


class AuthViewSet(viewsets.GenericViewSet):
    permission_classes = [AllowAny, ]
    serializer_class = serializers.EmptySerializer
    serializer_classes = {
        'login': serializers.EmployeeLoginSerializer,
        'register': serializers.EmployeeRegisterSerializer,
        'password_change': serializers.PasswordChangeSerializer,
    }

    @action(methods=['POST', ], detail=False)
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_and_authenticate_user(**serializer.validated_data)
        data = serializers.AuthSerializer(user).data
        return Response(data={"employee details":data, "message":"Login successful"}, status=status.HTTP_200_OK)


    @action(methods=['POST', ], detail=False)
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        email_exists = Employee.objects.filter(email = request.data.get('email'))
        if email_exists:
            user = email_exists[0]
        else:
            user = create_user_account(**serializer.validated_data)
        workspace = Workspace.objects.filter(id = request.data.get('workspace_id'))
        user.workspace.add(*workspace)
        data = serializers.AuthSerializer(user).data
        return Response(data=data, status=status.HTTP_201_CREATED)


    @action(methods=['POST', ], detail=False)
    def logout(self, request):
        logout(request)
        data = {'success': 'Sucessfully logged out'}
        return Response(data=data, status=status.HTTP_200_OK)

    @action(methods=['POST'], detail=False, permission_classes=[IsAuthenticated, ])
    def password_change(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        request.user.set_password(serializer.validated_data['new_password'])
        request.user.save()
        data = {'success': 'Sucessfully changed password'}
        return Response(data=data, status=status.HTTP_204_NO_CONTENT)

    def get_serializer_class(self):
        if not isinstance(self.serializer_classes, dict):
            raise ImproperlyConfigured("serializer_classes should be a dict mapping.")

        if self.action in self.serializer_classes.keys():
            return self.serializer_classes[self.action]
        return super().get_serializer_class()