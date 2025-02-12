# Generated by Django 5.1 on 2024-08-18 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0015_purchase_is_premium'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='jobs/')),
                ('title', models.CharField(max_length=200)),
                ('package', models.CharField(max_length=200)),
                ('requirements', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=1000)),
                ('date_posted', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
