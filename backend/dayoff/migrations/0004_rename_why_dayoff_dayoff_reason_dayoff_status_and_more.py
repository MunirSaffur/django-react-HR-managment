# Generated by Django 4.2.5 on 2023-10-11 09:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dayoff', '0003_alter_dayoff_why'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dayoff',
            old_name='why',
            new_name='dayoff_reason',
        ),
        migrations.AddField(
            model_name='dayoff',
            name='status',
            field=models.CharField(choices=[('in_review', 'In Review'), ('approved', 'Approved'), ('declined', 'Declined')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='dayoff',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
