from django.conf import settings
from .models import Employee


class EmailOrUsernameModelBackend(object):
    def authenticate(self, request, username=None, password=None):
        if '@' in username:
            kwargs = {'email': username}
        try:
            user = Employee.objects.get(**kwargs)
            if user.check_password(password):
                return user
        except Employee.DoesNotExist:
            return None

    def get_user(self, id):
        try:
            return Employee.objects.get(pk=id)
        except Employee.DoesNotExist:
            return None