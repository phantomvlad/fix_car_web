# Generated by Django 4.2.5 on 2023-09-19 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0011_alter_car_air_alter_car_engine_alter_car_gaz_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='air',
            field=models.CharField(blank=True, choices=[('atmo', 'Атмосферный'), ('turb', 'Турбированный')], max_length=5, verbose_name='Подача воздуха'),
        ),
        migrations.AlterField(
            model_name='car',
            name='engine',
            field=models.CharField(blank=True, choices=[('fuel', 'Бензин'), ('dise', 'Дизель'), ('elec', 'Элекрический')], max_length=5, verbose_name='Тип двигателя'),
        ),
        migrations.AlterField(
            model_name='car',
            name='transmission',
            field=models.CharField(blank=True, choices=[('auto', 'АКоробка-автомат'), ('mech', 'Механическая коробка'), ('robo', 'Роботизированная коробка')], max_length=5, verbose_name='Тип коробки передач'),
        ),
        migrations.AlterField(
            model_name='car',
            name='wheel_drive',
            field=models.CharField(blank=True, choices=[('front', 'Передний'), ('back', 'Задний'), ('full', 'Полный')], max_length=6, verbose_name='Привод'),
        ),
    ]
