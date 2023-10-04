from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

from cars.models import Car

TYPE_CHOICES = [
    ("repair", "Ремонт"),
    ("replace", "Замена"),
]
KIND_CHOICES = [
    ('engine', "Двигатель"),
    ("electro", "Электрика"),
    ("transmission", "Трансмиссия"),
    ('brakes', 'Тормоза'),
    ("suspension", 'Подвеска'),
    ('exhaust', 'Выхлоп'),
    ('other', 'Другое'),
]

class Repair(models.Model):
    title = models.CharField(verbose_name='Название ремонта')
    type = models.CharField(max_length=7, verbose_name='Ремонт/замена', choices=TYPE_CHOICES)
    kind = models.CharField(max_length=12, verbose_name='Тип ремонта', choices=KIND_CHOICES)
    date = models.DateField(verbose_name='Дата ремонта')
    description_small = models.CharField(max_length=250, verbose_name='Краткое описание')
    description_full = models.TextField(max_length=2000, verbose_name='Полное описание', null=True, blank=True)
    cause = models.CharField(max_length=500, verbose_name='Причина ремонта', default='Замена по плану')
    mileage = models.PositiveIntegerField(verbose_name='Пробег')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(get_user_model(), on_delete = models.SET_NULL, related_name='repairs', null=True, blank=True, verbose_name='Владелец', db_index=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='repairs', verbose_name='Автомобиль')

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('repair_show', kwargs={'pk_car': self.car.pk, 'pk_repair': self.pk})

    def save(self, *args, **kwargs):
        if not self.title:
            self.title = f'{self.description_small.capitalize()}, {self.mileage} км., {self.date.strftime("%d.%m.%Y")}'
        return super().save(*args, **kwargs)