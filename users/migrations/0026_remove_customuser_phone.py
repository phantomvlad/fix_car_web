# Generated by Django 4.2.5 on 2023-10-04 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_alter_customuser_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='phone',
        ),
    ]
