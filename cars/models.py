from django.db import models

from django.contrib.auth import get_user_model

class Car(models.Model):
    brand = models.CharField(verbose_name = 'brand')
    model = models.CharField()
    generation = models.IntegerField()
    transmission = models.CharField()
    engine = models.CharField()
    air = models.CharField()
    gaz = models.BooleanField()
    wheel_drive = models.CharField()
    capacity = models.IntegerField()
    mileage = models.IntegerField()
    vincode = models.CharField()
    owner = models.ForeignKey(get_user_model(), on_delete = models.SET_NULL, related_name='cars', null=True)


    def __str__(self):
        return f"{self.brand} {self.model} {self.generation}"