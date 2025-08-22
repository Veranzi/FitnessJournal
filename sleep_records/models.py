# models.py

from django.db import models
from django.contrib.auth.models import User

class SleepRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    hours_slept = models.DecimalField(max_digits=4, decimal_places=2)  # Hours slept
    quality = models.CharField(max_length=10)  # Sleep quality: "Good", "Fair", "Poor"
    notes = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.date}"
