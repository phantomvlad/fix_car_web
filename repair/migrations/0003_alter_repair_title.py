# Generated by Django 5.0 on 2023-12-08 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0002_alter_repair_mileage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repair',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Название ремонта'),
        ),
    ]