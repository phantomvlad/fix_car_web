# Generated by Django 4.2.5 on 2023-09-19 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_customuser_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='phone',
            field=models.CharField(blank=True, max_length=15, unique=True, verbose_name='Мобильный телефон'),
        ),
    ]