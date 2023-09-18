from django.db import models

from django.contrib.auth import get_user_model

class Car(models.Model):
    brand = models.CharField(verbose_name='Марка')
    model = models.CharField(verbose_name='Модель')
    photo = models.ImageField(default=None, verbose_name='Изображение авто')
    generation = models.IntegerField(verbose_name='Год выпуска')
    transmission = models.CharField(verbose_name='Тип коробки передач')
    engine = models.CharField(verbose_name='Тип двигателя')
    air = models.CharField(verbose_name='Подача воздуха')
    gaz = models.BooleanField(verbose_name='Газовое оборудование')
    wheel_drive = models.CharField(verbose_name='Привод')
    capacity = models.IntegerField(verbose_name='Мощность двигателя')
    mileage = models.IntegerField(verbose_name='Пробег')
    vincode = models.CharField(verbose_name='Винкод')
    owner = models.ForeignKey(get_user_model(), on_delete = models.SET_NULL, related_name='cars', null=True, verbose_name = 'Владелец')


    def __str__(self):
        return f"{self.brand} {self.model} {self.generation}"