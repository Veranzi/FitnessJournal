from django.urls import path
from . import views

urlpatterns = [
    path('add-meal/', views.add_meal, name='add_meal'),  # Add meal URL
    path('diet-log/', views.diet_log, name='diet_log'),  # Display diet log URL
]
