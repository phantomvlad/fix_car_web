# Generated by Django 5.0 on 2023-12-13 10:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0035_alter_car_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='thumbnails',
            field=models.ImageField(default='images/cars/default_car.jpg', upload_to='images/cars/thumbnails/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=('png', 'jpg', 'webp', 'jpeg'))], verbose_name='Изображение авто mini'),
        ),
    ]
