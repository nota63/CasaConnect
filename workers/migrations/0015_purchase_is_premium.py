# Generated by Django 5.1 on 2024-08-18 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0014_purchase_premium_card'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='is_premium',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
