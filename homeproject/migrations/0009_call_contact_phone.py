# Generated by Django 5.1 on 2024-08-29 09:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeproject', '0008_rename_project_call_project_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='call',
            name='contact_phone',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contact_calls', to='homeproject.homeproject'),
        ),
    ]