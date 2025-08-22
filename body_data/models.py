# models.py
from django.db import models
from django.contrib.auth.models import User

class BodyData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)  # Weight in kilograms
    chest = models.DecimalField(max_digits=5, decimal_places=2)  # Chest circumference in cm
    waist = models.DecimalField(max_digits=5, decimal_places=2)  # Waist circumference in cm
    hips = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Hips circumference in cm
    notes = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.date}"
