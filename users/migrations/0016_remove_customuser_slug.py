# Generated by Django 4.2.5 on 2023-09-26 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_alter_customuser_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='slug',
        ),
    ]
