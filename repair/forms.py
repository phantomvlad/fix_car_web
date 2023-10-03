from django.forms import ModelForm
from .models import Repair
from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput

class RepairForm(ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Repair
        exclude = ['title', 'car', 'owner']
        widgets ={
            "date": forms.DateInput(attrs={'type': 'date'})
        }