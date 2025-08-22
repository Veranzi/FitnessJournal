from django.db import models
from django.contrib.auth.models import User
from datetime import date

class TrainingPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    progress = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    goal = models.CharField(max_length=255, blank=True, null=True)  # New goal field
    notes = models.TextField(blank=True, null=True)  # New field for additional notes

    
    def __str__(self):
        return f"{self.name} - {self.user.username} (from {self.start_date} to {self.end_date})"

class TrainingSession(models.Model):
    plan = models.ForeignKey(TrainingPlan, on_delete=models.CASCADE, related_name='sessions')
    day = models.CharField(max_length=50)  # E.g., "Week 1, Day 1"
    exercises = models.TextField()  # A description of exercises for the session
    target_sets = models.IntegerField()  # E.g., number of sets for each exercise
    target_reps = models.IntegerField()  # E.g., reps per set
    target_weight = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    completed = models.BooleanField(default=False)  # Add a completed field
    due_date = models.DateField(default=date.today)  # Set default to today's date

    def __str__(self):
        return f"Session for {self.plan.name} on {self.day} (Due: {self.due_date})"