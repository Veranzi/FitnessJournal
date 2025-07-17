from django.db import models
from django.contrib.auth.models import User

class WorkoutRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.CharField(max_length=100)  # Exercise name (e.g., Squats, Deadlifts)
    sets = models.IntegerField()  # Number of sets performed
    reps = models.IntegerField()  # Number of reps per set
    weight = models.DecimalField(max_digits=5, decimal_places=2)  # Weight lifted (e.g., 100.00 kg)
    date = models.DateField()  # Date of the workout
    notes = models.TextField(blank=True)  # Optional notes (e.g., "Felt strong today")

    def __str__(self):
        return f'{self.exercise} on {self.date}'
