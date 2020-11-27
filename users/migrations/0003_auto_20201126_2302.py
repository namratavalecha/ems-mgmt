# Generated by Django 3.0 on 2020-11-26 23:02

from django.db import migrations, models
import django.utils.timezone
import users.managers


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0002_auto_20201126_1943'),
        ('users', '0002_auto_20201126_2148'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='employee',
            managers=[
                ('objects', users.managers.EmployeeManager()),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_login',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='workspace',
            field=models.ManyToManyField(blank=True, to='workspace.Workspace'),
        ),
    ]