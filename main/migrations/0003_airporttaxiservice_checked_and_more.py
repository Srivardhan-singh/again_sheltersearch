# Generated by Django 4.1.7 on 2023-04-02 09:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_user_airporttaxiservice_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='airporttaxiservice',
            name='checked',
            field=models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=5),
        ),
        migrations.AddField(
            model_name='airporttaxiservice',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='airporttaxiservice',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Regret', 'Regret'), ('Completed', 'Completed')], default='Pending', max_length=20),
        ),
        migrations.AddField(
            model_name='airporttaxiservice',
            name='travel_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='airporttaxiservice',
            name='travel_time',
            field=models.TimeField(default='21:00'),
            preserve_default=False,
        ),
    ]