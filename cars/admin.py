from django.contrib import admin
from .models import Car

class CarInline(admin.TabularInline):
    model = Car

class CarAdmin(admin.ModelAdmin):
    model = Car
    list_display = ('__str__', 'owner', 'time_create', 'time_update',)
    ordering = ('-time_update',)

admin.site.register(Car, CarAdmin)