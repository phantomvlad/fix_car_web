from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

class Car(models.Model):
    brand = models.CharField(verbose_name='Марка')
    model = models.CharField(verbose_name='Модель')
    generation = models.PositiveSmallIntegerField(verbose_name='Год выпуска')
    transmission = models.CharField(verbose_name='Тип коробки передач', blank=True)
    engine = models.CharField(verbose_name='Тип двигателя', blank=True)
    air = models.CharField(verbose_name='Подача воздуха', blank=True)
    gaz = models.BooleanField(verbose_name='Газовое оборудование', blank=True)
    wheel_drive = models.CharField(verbose_name='Привод', blank=True)
    capacity = models.PositiveSmallIntegerField(verbose_name='Мощность двигателя', blank=True)
    mileage = models.PositiveIntegerField(verbose_name='Пробег', blank=True)
    vincode = models.CharField(verbose_name='Винкод', null=True, unique=True)
    owner = models.ForeignKey(get_user_model(), on_delete = models.SET_NULL, related_name='cars', null=True, verbose_name='Владелец')

    def __str__(self):
        return f"{self.brand} {self.model} {self.generation}"

    def get_absolute_url(self):
        return reverse('car_show', kwargs={'pk': self.pk})