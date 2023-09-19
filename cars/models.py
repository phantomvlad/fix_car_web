from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

TRANSMISSION_CHOICES = [
    ("auto", "Автомат"),
    ("mech", "Механическая коробка"),
    ("robo", "Робот"),
]
ENGINE_CHOICES = [
    ('fuel', "Бензин"),
    ("dise", "Дизель"),
    ("elec", "Электрический"),
]
AIR_CHOICES = [
    ("atmo", "Атмосферный"),
    ("turb", "Турбированный")
]
WHEEL_CHOICES = [
    ("front", "Передний"),
    ("back", "Задний"),
    ("full", "Полный")
]

class Car(models.Model):
    brand = models.CharField(verbose_name='Марка')
    model = models.CharField(verbose_name='Модель')
    generation = models.PositiveSmallIntegerField(verbose_name='Год выпуска')
    transmission = models.CharField(verbose_name='Тип коробки передач', null=True, blank=True, choices=TRANSMISSION_CHOICES, max_length=4)
    engine = models.CharField(verbose_name='Тип двигателя', null=True, blank=True, choices=ENGINE_CHOICES, max_length=4)
    air = models.CharField(verbose_name='Подача воздуха', null=True, blank=True, choices=AIR_CHOICES, max_length=4)
    gaz = models.BooleanField(verbose_name='Газовое оборудование', null=True, blank=True, default=False)
    wheel_drive = models.CharField(verbose_name='Привод', null=True, blank=True, choices=WHEEL_CHOICES, max_length=5)
    capacity = models.PositiveSmallIntegerField(verbose_name='Мощность двигателя', null=True, blank=True)
    mileage = models.PositiveIntegerField(verbose_name='Пробег', null=True, blank=True)
    vincode = models.CharField(verbose_name='Винкод', null=True, blank=True)
    owner = models.ForeignKey(get_user_model(), on_delete = models.SET_NULL, related_name='cars', null=True, blank=True, verbose_name='Владелец')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['vincode'], name='unique_vincode')
        ]

    def __str__(self):
        return f"{self.brand} {self.model} {self.generation}"

    def get_absolute_url(self):
        return reverse('car_show', kwargs={'pk': self.pk})