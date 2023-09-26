from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.template.defaultfilters import slugify

class CustomUser(AbstractUser):
    phone = PhoneNumberField(verbose_name="Мобильный телефон")
    slug_username = models.SlugField(unique=True, max_length=255, db_index=True, null=False)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('account_show', kwargs={'slug_username': self.slug_username})

    def save(self, *args, **kwargs):
        if not self.slug_username:
            self.slug_username = slugify(self.username)
        return super().save(*args, **kwargs)