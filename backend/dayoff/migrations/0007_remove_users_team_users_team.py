# Generated by Django 4.2.5 on 2023-10-28 08:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dayoff', '0006_users_team'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='team',
        ),
        migrations.AddField(
            model_name='users',
            name='team',
            field=models.ManyToManyField(blank=True, null=True, related_name='selected_by_users', to=settings.AUTH_USER_MODEL),
        ),
    ]
