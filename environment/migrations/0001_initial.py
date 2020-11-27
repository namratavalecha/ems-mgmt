# Generated by Django 3.0 on 2020-11-27 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('workspace', '0003_auto_20201127_0106'),
    ]

    operations = [
        migrations.CreateModel(
            name='Environment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('slack_username', models.CharField(blank=True, max_length=100, null=True)),
                ('slack_channel', models.CharField(blank=True, max_length=100, null=True)),
                ('slack_token', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('workspace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workspace.Workspace')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]
