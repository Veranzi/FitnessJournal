from django.shortcuts import render, redirect
from .forms import WorkoutRecordForm
from django.contrib.auth.decorators import login_required
from .models import WorkoutRecord

@login_required
def add_workout(request):
    if request.method == 'POST':
        form = WorkoutRecordForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)  # Do not save immediately
            workout.user = request.user  # Associate workout with the logged-in user
            workout.save()  # Save the workout to the database
            return redirect('training_records')  # Redirect to the training records page
    else:
        form = WorkoutRecordForm()  # Display an empty form

    return render(request, 'add_workout.html', {'form': form})

@login_required
def training_records(request):
    # Fetch all workout records for the logged-in user
    workout_records = WorkoutRecord.objects.filter(user=request.user)
    return render(request, 'training_records.html', {'workout_records': workout_records})
