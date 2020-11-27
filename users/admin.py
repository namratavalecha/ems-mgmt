from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Employee
from .forms import EmployeeForm
from django.contrib.sites.models import Site
from django.contrib import auth
# from rest_framework.authtoken.models import Token

admin.site.site_title = "EMS Admin Portal"
admin.site.site_header = "EMS Admin"

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    form = EmployeeForm

    fields = ('email', 'password', 'workspace', 'name', 'role', 'is_staff', 'is_active', 'is_superuser', 'designation', \
        'phone_number', 'github_username', 'slack_username', 'slack_user_id', 'date_joined', 'last_login', 'groups', 'user_permissions')
    list_display = ['email', 'name']
    ordering = ('email',)

admin.site.register(Employee, EmployeeAdmin)
admin.site.unregister(Site)
admin.site.unregister(auth.models.Group)
# admin.site.unregister(Token)