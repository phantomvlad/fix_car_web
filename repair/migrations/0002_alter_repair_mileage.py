# Generated by Django 4.2.5 on 2023-09-26 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repair',
            name='mileage',
            field=models.PositiveIntegerField(verbose_name='Пробег'),
        ),
    ]
