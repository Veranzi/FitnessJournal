from django.shortcuts import render, redirect
from .forms import MealForm
from .models import Meal
from django.contrib.auth.decorators import login_required

@login_required
def add_meal(request):
    if request.method == 'POST':
        form = MealForm(request.POST)
        if form.is_valid():
            meal = form.save(commit=False)  # Don't save immediately
            meal.user = request.user  # Associate the meal with the logged-in user
            meal.save()  # Save the meal to the database
            return redirect('diet_log')  # Redirect to the diet log page
    else:
        form = MealForm()  # Display an empty form

    return render(request, 'add_meal.html', {'form': form})

@login_required
def diet_log(request):
    # Fetch all meal records for the logged-in user
    meals = Meal.objects.filter(user=request.user)
    return render(request, 'diet_log.html', {'meals': meals})
