from django.db import models
from django.contrib.auth.models import User

class Meal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link meal to user
    food_item = models.CharField(max_length=255)  # Name of the food item
    calories = models.IntegerField()  # Calories for the meal
    carbs = models.DecimalField(max_digits=5, decimal_places=2)  # Carbs in grams
    protein = models.DecimalField(max_digits=5, decimal_places=2)  # Protein in grams
    fat = models.DecimalField(max_digits=5, decimal_places=2)  # Fat in grams
    meal_type = models.CharField(max_length=20, choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner')])  # Type of meal
    date = models.DateField()  # Date of the meal entry
    notes = models.TextField(blank=True)  # Optional notes

    def __str__(self):
        return f'{self.food_item} - {self.meal_type} on {self.date}'
