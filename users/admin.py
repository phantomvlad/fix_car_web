from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from cars.admin import CarInline
from repair.admin import RepairInline

from .forms import CustomUserChangeForm, CustomUserCreationForm
# Register your models here.

CustomUser = get_user_model()

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    prepopulated_fields = {"slug": ('username', )}
    fieldsets = None
    fields = ("email", 'username', 'phone',)

    inlines = [
        CarInline,
        RepairInline
    ]
    list_display = ["email", 'username', 'phone', 'time_create', 'time_update', 'slug']


admin.site.register(CustomUser, CustomUserAdmin)