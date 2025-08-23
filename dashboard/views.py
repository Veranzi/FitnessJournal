from django.shortcuts import render
from body_data.models import BodyData
from diet_records.models import Meal
from sleep_records.models import SleepRecord
from training_records.models import WorkoutRecord
from django.http import JsonResponse

# Dashboard View
def dashboard(request):
    body_data = BodyData.objects.filter(user=request.user).order_by('-date')
    meals = Meal.objects.filter(user=request.user).order_by('-date')
    sleep_records = SleepRecord.objects.filter(user=request.user).order_by('-date')
    workouts = WorkoutRecord.objects.filter(user=request.user).order_by('-date')

    # Fetch recent data for charts (e.g., last 30 days)
    chart_data = {
        'body_data': list(body_data.values('date', 'weight', 'chest', 'waist', 'hips')),
        'meals': list(meals.values('date', 'calories', 'carbohydrates', 'protein', 'fat')),
        'sleep': list(sleep_records.values('date', 'hours_slept', 'quality')),
        'workouts': list(workouts.values('date', 'weight')),
    }

    return render(request, 'dashboard.html', {'chart_data': chart_data})

# API endpoint for getting chart data
def get_chart_data(request):
    body_data = BodyData.objects.filter(user=request.user).order_by('-date')[:30]
    meals = Meal.objects.filter(user=request.user).order_by('-date')[:30]
    sleep_records = SleepRecord.objects.filter(user=request.user).order_by('-date')[:30]
    workouts = WorkoutRecord.objects.filter(user=request.user).order_by('-date')[:30]

    chart_data = {
        'body_data': list(body_data.values('date', 'weight', 'chest', 'waist', 'hips')),
        'meals': list(meals.values('date', 'calories', 'carbohydrates', 'protein', 'fat')),
        'sleep': list(sleep_records.values('date', 'hours_slept', 'quality')),
        'workouts': list(workouts.values('date', 'weight')),
    }

    return JsonResponse(chart_data)
