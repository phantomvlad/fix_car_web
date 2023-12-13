# Generated by Django 5.0 on 2023-12-13 06:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0028_alter_car_brand_alter_car_model_alter_car_vincode'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/cars/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=('png', 'jpg', 'webp', 'jpeg'))], verbose_name='Изображение авто'),
        ),
    ]