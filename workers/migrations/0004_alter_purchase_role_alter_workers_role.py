# Generated by Django 5.1 on 2024-08-14 11:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0003_purchase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='role',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='workers.role'),
        ),
        migrations.AlterField(
            model_name='workers',
            name='role',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='workers.role'),
        ),
    ]
