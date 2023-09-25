# Generated by Django 4.2.5 on 2023-09-25 12:41

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_customuser_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Мобильный телефон'),
        ),
    ]
