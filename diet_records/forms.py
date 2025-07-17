from django import forms
from .models import Meal

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['food_item', 'calories', 'carbs', 'protein', 'fat', 'meal_type', 'date', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),  # Render date as a date picker
            'notes': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter any additional notes here...'}),
        }
