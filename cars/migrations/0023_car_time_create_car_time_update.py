# Generated by Django 4.2.5 on 2023-09-25 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0022_alter_car_air_alter_car_capacity_alter_car_engine_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='time_update',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]