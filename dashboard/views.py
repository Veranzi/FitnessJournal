from django.shortcuts import render
from body_data.models import BodyData
from diet_records.models import Meal
from sleep_records.models import SleepRecord
from training_records.models import WorkoutRecord
from django.http import JsonResponse

# Utility function to format date
def format_queryset(qs, fields):
    data = []
    for obj in qs:
        item = {}
        for field in fields:
            value = getattr(obj, field)
            if field == "date":  # Format date here
                value = value.strftime("%d-%m-%Y")
            item[field] = value
        data.append(item)
    return data

# Dashboard View
def dashboard(request):
    body_data = BodyData.objects.filter(user=request.user).order_by('-date')
    meals = Meal.objects.filter(user=request.user).order_by('-date')
    sleep_records = SleepRecord.objects.filter(user=request.user).order_by('-date')
    workouts = WorkoutRecord.objects.filter(user=request.user).order_by('-date')

    chart_data = {
        'body_data': format_queryset(body_data, ['date', 'weight', 'chest', 'waist', 'hips']),
        'meals': format_queryset(meals, ['date', 'calories', 'carbohydrates', 'protein', 'fat']),
        'sleep': format_queryset(sleep_records, ['date', 'hours_slept', 'quality']),
        'workouts': format_queryset(workouts, ['date', 'weight']),
    }

    return render(request, 'dashboard.html', {'chart_data': chart_data})

# API endpoint for getting chart data
def get_chart_data(request):
    body_data = BodyData.objects.filter(user=request.user).order_by('-date')[:30]
    meals = Meal.objects.filter(user=request.user).order_by('-date')[:30]
    sleep_records = SleepRecord.objects.filter(user=request.user).order_by('-date')[:30]
    workouts = WorkoutRecord.objects.filter(user=request.user).order_by('-date')[:30]

    chart_data = {
        'body_data': format_queryset(body_data, ['date', 'weight', 'chest', 'waist', 'hips']),
        'meals': format_queryset(meals, ['date', 'calories', 'carbohydrates', 'protein', 'fat']),
        'sleep': format_queryset(sleep_records, ['date', 'hours_slept', 'quality']),
        'workouts': format_queryset(workouts, ['date', 'weight']),
    }

    return JsonResponse(chart_data)
