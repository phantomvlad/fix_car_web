# Generated by Django 4.2.5 on 2023-09-26 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_remove_customuser_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='slug',
            field=models.SlugField(default='phantom', max_length=255, unique=True),
        ),
    ]
