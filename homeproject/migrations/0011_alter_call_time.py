# Generated by Django 5.1 on 2024-08-30 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeproject', '0010_call_requested_call'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='time',
            field=models.CharField(blank=True, choices=[('next 30 minutes', 'next 30 minutes'), ('after an hour', 'after an hour'), ('tomorrow', 'tomorrow'), ('after 2 hours', 'after 2 hours')], max_length=100),
        ),
    ]