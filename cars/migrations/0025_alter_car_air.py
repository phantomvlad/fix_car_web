# Generated by Django 4.2.5 on 2023-10-02 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0024_alter_car_time_create_alter_car_time_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='air',
            field=models.CharField(blank=True, choices=[('atmo', 'Атмосферный'), ('turb', 'Турбированный')], max_length=4, null=True, verbose_name='Тип двигателя по подаче воздуха'),
        ),
    ]
