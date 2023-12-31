# Generated by Django 4.2.5 on 2023-10-04 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dayoff', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dayoff',
            name='end_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='dayoff',
            name='off_type',
            field=models.CharField(choices=[('annual', 'Annual Leave'), ('bounce', 'Bounce Leave'), ('no_paid', 'No Paid Vacation')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='dayoff',
            name='start_date',
            field=models.DateTimeField(null=True),
        ),
    ]
