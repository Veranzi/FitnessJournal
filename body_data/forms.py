# forms.py
from django import forms
from .models import BodyData

class BodyDataForm(forms.ModelForm):
    class Meta:
        model = BodyData
        fields = ['date', 'weight', 'chest', 'waist', 'hips', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'weight': forms.NumberInput(attrs={'step': '0.01'}),
            'chest': forms.NumberInput(attrs={'step': '0.01'}),
            'waist': forms.NumberInput(attrs={'step': '0.01'}),
            'hips': forms.NumberInput(attrs={'step': '0.01'}),
        }
