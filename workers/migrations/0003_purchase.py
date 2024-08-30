# Generated by Django 5.1 on 2024-08-14 10:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0002_workers_age'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=1000)),
                ('nearest_location', models.CharField(max_length=500)),
                ('payment', models.CharField(choices=[('cash', 'cash')], max_length=400)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workers.role')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workers.workers')),
            ],
        ),
    ]