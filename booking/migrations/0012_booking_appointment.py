# Generated by Django 5.0.6 on 2024-05-17 09:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0011_remove_booking_booking_date_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='appointment',
            field=models.OneToOneField(default=4, on_delete=django.db.models.deletion.DO_NOTHING, to='booking.appointments'),
            preserve_default=False,
        ),
    ]
