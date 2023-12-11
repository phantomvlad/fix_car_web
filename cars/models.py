from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

TRANSMISSION_CHOICES = [
    ("автомат", "Автомат"),
    ("механика", "Механическая коробка"),
    ("робот", "Робот"),
]
ENGINE_CHOICES = [
    ('бензин', "Бензин"),
    ("дизель", "Дизель"),
    ("электрический", "Электрический"),
]
AIR_CHOICES = [
    ("атмосферный", "Атмосферный"),
    ("турбированный", "Турбированный")
]
WHEEL_CHOICES = [
    ("передний", "Передний"),
    ("задний", "Задний"),
    ("полный", "Полный")
]

class Car(models.Model):
    brand = models.CharField(verbose_name='Марка', max_length=150)
    model = models.CharField(verbose_name='Модель', max_length=150)
    generation = models.PositiveSmallIntegerField(verbose_name='Год выпуска')
    transmission = models.CharField(verbose_name='Тип коробки передач', null=True, blank=True, choices=TRANSMISSION_CHOICES)
    engine = models.CharField(verbose_name='Тип двигателя', null=True, blank=True, choices=ENGINE_CHOICES)
    air = models.CharField(verbose_name='Тип двигателя по подаче воздуха', null=True, blank=True, choices=AIR_CHOICES)
    gaz = models.BooleanField(verbose_name='Газовое оборудование', null=True, blank=True, default=False)
    wheel_drive = models.CharField(verbose_name='Привод', null=True, blank=True, choices=WHEEL_CHOICES)
    capacity = models.PositiveSmallIntegerField(verbose_name='Мощность двигателя', null=True, blank=True)
    mileage = models.PositiveIntegerField(verbose_name='Пробег', null=True, blank=True)
    vincode = models.CharField(verbose_name='Винкод', null=True, blank=True, max_length=150)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(get_user_model(), on_delete = models.SET_NULL, related_name='cars', null=True, blank=True, verbose_name='Владелец', db_index=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['vincode'], name='unique_vincode')
        ]

    def __str__(self):
        return f"{self.brand} {self.model}"

    def get_absolute_url(self):
        return reverse('cars:show', kwargs={'pk': self.pk})