# Generated by Django 5.0 on 2023-12-13 09:42

import django.core.files.storage
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0032_alter_car_capacity_alter_car_generation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(default='images/cars/default_car.jpg', storage=django.core.files.storage.FileSystemStorage(), upload_to='images/cars/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=('png', 'jpg', 'webp', 'jpeg'))], verbose_name='Изображение авто'),
        ),
    ]
