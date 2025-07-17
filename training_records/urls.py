from django.urls import path
from . import views

urlpatterns = [
    path('add-workout/', views.add_workout, name='add_workout'),  # Add workout URL
    path('training-records/', views.training_records, name='training_records'),  # Training records URL
]
