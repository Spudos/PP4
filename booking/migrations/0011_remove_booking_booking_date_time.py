# Generated by Django 5.0.6 on 2024-05-17 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0010_remove_appointments_date_remove_appointments_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='booking_date_time',
        ),
    ]
