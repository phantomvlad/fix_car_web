from django.db import models
from django.dispatch import receiver
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.template.defaultfilters import slugify
from django.core.validators import RegexValidator
from allauth.account.models import EmailAddress
from allauth.account.signals import email_confirmed

class CustomUser(AbstractUser):
    slug = models.SlugField(unique=True, max_length=255, db_index=True, null=False)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('account_show', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        return super().save(*args, **kwargs)