# forms.py

from django import forms
from .models import SleepRecord

class SleepRecordForm(forms.ModelForm):
    class Meta:
        model = SleepRecord
        fields = ['date', 'hours_slept', 'quality', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'hours_slept': forms.NumberInput(attrs={'step': '0.01'}),
        }
