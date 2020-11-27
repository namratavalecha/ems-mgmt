# Generated by Django 3.0 on 2020-11-27 06:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('environment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('environment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='environment.Environment')),
                ('members', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
