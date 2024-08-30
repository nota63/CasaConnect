# Generated by Django 5.1 on 2024-08-28 10:08

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0020_discounts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discounts',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='discounts',
            name='link',
            field=models.CharField(max_length=1000),
        ),
    ]
