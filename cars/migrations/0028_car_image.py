# Generated by Django 4.2.6 on 2023-10-04 17:03

from django.db import migrations, models
import storages.backends.s3


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0027_alter_car_air_alter_car_engine_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='image',
            field=models.ImageField(default=None, storage=storages.backends.s3.S3Storage(), upload_to='images/'),
            preserve_default=False,
        ),
    ]
