from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from workspace.models import Workspace
from django.core.validators import RegexValidator
from .managers import EmployeeManager
from django.utils import timezone

# Create your models here.

class Employee(AbstractBaseUser, PermissionsMixin):
    role_choices = [
        ('org_admin', 'Organization admin'),
        ('site_admin', 'Site admin'),
        ('member', 'Member')
    ]
    email = models.EmailField(unique=True)
    workspace = models.ManyToManyField(Workspace, blank=True)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=30, choices=role_choices, default='member')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    designation = models.CharField(max_length=40, null=True, blank=True)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True, null=True)
    github_username = models.CharField(max_length=100, null=True, blank=True)
    slack_username = models.CharField(max_length=100, null=True, blank=True)
    slack_user_id = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = EmployeeManager()

    def __str__(self):
        return (self.email)

    class Meta:
        ordering = ('-created_at',)

