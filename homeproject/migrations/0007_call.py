# Generated by Django 5.1 on 2024-08-29 09:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeproject', '0006_homeproject_company_budget_homeproject_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Call',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(choices=[('next 30 minutes', 'next 30 minutes'), ('after an hour', 'after an hour'), ('tomorrow', 'tomorrow'), ('after 2 hours', 'after 2 hours')], max_length=100)),
                ('or_specified_time', models.CharField(blank=True, max_length=100)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homeproject.homeproject')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]