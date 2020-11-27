from django.db import models
from environment.models import Environment
from users.models import Employee
from django.db.models import signals
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=100)
    environment = models.OneToOneField(Environment, on_delete=models.CASCADE)
    members = models.ManyToManyField(Employee, blank=True)

    def __str__(self):
        return (self.name)


@receiver(post_save, sender=Environment)
def create_team(sender, instance, **kwargs):
    name = instance.name
    team = Team(name = name+" Team", environment=instance)
    team.save()