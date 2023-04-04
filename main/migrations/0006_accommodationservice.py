# Generated by Django 4.1.7 on 2023-04-03 04:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0005_alter_airporttaxiservice_order_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccommodationService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accommodation_type', models.CharField(max_length=20)),
                ('occupancy', models.CharField(max_length=15)),
                ('move_in_date', models.DateField()),
                ('gender', models.CharField(blank=True, max_length=7, null=True)),
                ('address', models.CharField(max_length=200)),
                ('order_id', models.CharField(max_length=50, unique=True)),
                ('checked', models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=5)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
