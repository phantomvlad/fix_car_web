from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, verbose_name="Мобильный телефон", unique=True)
    slug = models.SlugField(unique=True, max_length=255, db_index=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('account_show', kwargs={'slug': self.slug})