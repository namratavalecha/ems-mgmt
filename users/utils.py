from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import Employee

def get_and_authenticate_user(email, password):
    user = authenticate(username=email, password=password)
    if user is None:
        raise serializers.ValidationError("Invalid username/password. Please try again!")
    return user

def create_user_account(email, password, **extra_fields):
    user = Employee.objects.create_user(
        email=email, password=password, **extra_fields)
    return user