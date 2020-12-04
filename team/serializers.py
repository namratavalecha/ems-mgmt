from rest_framework import serializers
from .models import Team
from environment.models import Environment
from users.models import Employee


class TeamSerializer(serializers.ModelSerializer):

    def validate(self, data):
        env_workspace = Environment.objects.filter(id=self.initial_data['environment']).values('workspace__id')
        for employee_id in self.initial_data['members']:
            emp_workspace = Employee.objects.filter(id=employee_id).values('workspace__id')
            if(env_workspace.intersection(emp_workspace).count() == 0):
                raise serializers.ValidationError("Please add all employees to workspace first.")
        return data

    class Meta:
        model = Team
        fields = '__all__'