from django import forms
from .models import WorkoutRecord
from datetime import date


class WorkoutRecordForm(forms.ModelForm):
    class Meta:
        model = WorkoutRecord
        fields = ['exercise', 'sets', 'reps', 'weight', 'date', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'max': date.today().strftime('%Y-%m-%d')}),
            'notes': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter any additional notes here...'}),
        }
