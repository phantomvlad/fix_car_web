# Generated by Django 4.2.5 on 2023-09-19 10:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0015_alter_car_air_alter_car_engine_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='generation',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1940), django.core.validators.MaxValueValidator(2023)], verbose_name='Год выпуска'),
        ),
    ]