# Generated by Django 5.0.6 on 2024-05-16 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_remove_booking_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
