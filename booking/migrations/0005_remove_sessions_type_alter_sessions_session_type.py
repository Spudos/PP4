# Generated by Django 5.0.6 on 2024-05-15 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_sessions_session_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sessions',
            name='type',
        ),
        migrations.AlterField(
            model_name='sessions',
            name='session_type',
            field=models.TextField(choices=[('Gym', 'Gym'), ('Strength', 'Strength'), ('Cardio', 'Cardio'), ('Nutrition', 'Nutrition'), ('Motivation', 'Motivation'), ('Weight Loss', 'Weight Loss')], default='Gym'),
        ),
    ]