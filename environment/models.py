from django.db import models
from workspace.models import Workspace


# Create your models here.

class Environment(models.Model):
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    slack_username = models.CharField(max_length=100, null=True, blank=True)
    slack_channel = models.CharField(max_length=100, null=True, blank=True)
    slack_token = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.name)

    class Meta:
        ordering = ('-created_at',)

