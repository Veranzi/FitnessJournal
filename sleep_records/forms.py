# forms.py

from django import forms
from .models import SleepRecord
from datetime import date


class SleepRecordForm(forms.ModelForm):
    class Meta:
        model = SleepRecord
        fields = ['date', 'hours_slept', 'quality', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'max': date.today().strftime('%Y-%m-%d')}),
            'hours_slept': forms.NumberInput(attrs={'step': '0.01'}),
        }
