# Generated by Django 4.2.5 on 2023-09-18 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_car_photo_alter_car_air_alter_car_brand_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='photo',
            field=models.ImageField(default=None, null=True, upload_to='image/cars/', verbose_name='Изображение авто'),
        ),
    ]
