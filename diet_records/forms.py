from django import forms
from .models import Meal
from datetime import date


class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['food_item', 'calories', 'carbohydrates', 'protein', 'fat', 'meal_type', 'date', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'max': date.today().strftime('%Y-%m-%d')}),
            'notes': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter any additional notes here...'}),
        }
