# Generated by Django 4.2.5 on 2023-09-25 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_customuser_time_create_customuser_time_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='time_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
