from django.forms import ModelForm
from .models import Car
from django.core.validators import EmailValidator
from django import forms
class CarForm(ModelForm):
    class Meta:
        model = Car
        exclude = ['owner']
        widgets = {
            'gaz': forms.RadioSelect(choices=((True, 'Да'), (False, 'Нет')))
        }

        help_texts = {
            'gaz': 'Выберите, есть ли у вас газовое оборудование'
        }

