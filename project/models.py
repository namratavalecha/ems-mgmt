from django.db import models
from environment.models import Environment
from users.models import Employee

# Create your models here.

class Project(models.Model):
    environment = models.ForeignKey(Environment, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    github_url = models.CharField(blank=True, null=True, max_length=150)
    jira_url = models.CharField(max_length=150, null=True, blank=True)
    team_members = models.ManyToManyField(Employee, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.name)