from django.contrib import admin
from .models import Car

class CarInline(admin.TabularInline):
    model = Car

admin.site.register(Car)