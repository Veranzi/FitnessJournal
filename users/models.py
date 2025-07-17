from django.db import models
from django.contrib.auth.models import AbstractUser

# Optionally, you can extend AbstractUser to add more fields to your user model
class CustomUser(AbstractUser):
    pass  # Add any additional fields you need, like profile picture, bio, etc.

