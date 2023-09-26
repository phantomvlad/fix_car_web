from django.contrib import admin
from .models import Repair
from .forms import RepairForm
class RepairInline(admin.TabularInline):
    model = Repair

class RepairAdmin(admin.ModelAdmin):
    model = Repair
    form = RepairForm
    list_display = ('__str__', 'owner', 'car', 'time_create', 'time_update',)
    ordering = ('-time_update',)

admin.site.register(Repair, RepairAdmin)