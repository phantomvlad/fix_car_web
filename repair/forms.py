from django.forms import ModelForm
from .models import Repair

class RepairForm(ModelForm):
    class Meta:
        model = Repair
        exclude = ['title', 'car', 'owner']

