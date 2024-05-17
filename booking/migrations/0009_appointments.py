# Generated by Django 5.0.6 on 2024-05-16 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0008_booking_approved'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_type', models.TextField(default='General')),
                ('available', models.BooleanField(default=True)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
    ]