from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    car = models.CharField(max_length=30, default='')
    pass
