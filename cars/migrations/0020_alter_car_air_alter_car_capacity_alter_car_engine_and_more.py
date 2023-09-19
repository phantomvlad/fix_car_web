# Generated by Django 4.2.5 on 2023-09-19 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0019_alter_car_vincode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='air',
            field=models.CharField(choices=[('atmo', 'Атмосферный'), ('turb', 'Турбированный')], max_length=4, null=True, verbose_name='Подача воздуха'),
        ),
        migrations.AlterField(
            model_name='car',
            name='capacity',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='Мощность двигателя'),
        ),
        migrations.AlterField(
            model_name='car',
            name='engine',
            field=models.CharField(choices=[('fuel', 'Бензин'), ('dise', 'Дизель'), ('elec', 'Электрический')], max_length=4, null=True, verbose_name='Тип двигателя'),
        ),
        migrations.AlterField(
            model_name='car',
            name='gaz',
            field=models.BooleanField(default=False, null=True, verbose_name='Газовое оборудование'),
        ),
        migrations.AlterField(
            model_name='car',
            name='mileage',
            field=models.PositiveIntegerField(null=True, verbose_name='Пробег'),
        ),
        migrations.AlterField(
            model_name='car',
            name='transmission',
            field=models.CharField(choices=[('auto', 'Автомат'), ('mech', 'Механическая коробка'), ('robo', 'Робот')], max_length=4, null=True, verbose_name='Тип коробки передач'),
        ),
        migrations.AlterField(
            model_name='car',
            name='vincode',
            field=models.CharField(null=True, unique=True, verbose_name='Винкод'),
        ),
        migrations.AlterField(
            model_name='car',
            name='wheel_drive',
            field=models.CharField(choices=[('front', 'Передний'), ('back', 'Задний'), ('full', 'Полный')], max_length=5, null=True, verbose_name='Привод'),
        ),
        migrations.AddConstraint(
            model_name='car',
            constraint=models.UniqueConstraint(fields=('vincode',), name='unique_vincode'),
        ),
    ]
