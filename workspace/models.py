import uuid
from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Workspace(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64)
    email = models.EmailField(unique=False)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True)
    url = models.CharField(blank=True, max_length=64)
    location = models.CharField(blank=True, max_length=240)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.name)

    class Meta:
        ordering = ('-created_at',)