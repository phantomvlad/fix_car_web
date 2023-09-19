from django.forms import ModelForm
from .models import Car
from django.core.validators import EmailValidator
class CarForm(ModelForm):
    class Meta:
        model = Car
        exclude = ['owner']

    