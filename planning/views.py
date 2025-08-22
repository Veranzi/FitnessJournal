from django.shortcuts import render, get_object_or_404, redirect
from .models import TrainingPlan, TrainingSession
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta

# View to display all training plans for a user
@login_required
def training_plans(request):
    plans = TrainingPlan.objects.filter(user=request.user)
    return render(request, 'training_plans.html', {'plans': plans})

# View to display the details of a specific training plan and its sessions
@login_required
def training_plan_sessions(request, plan_id):
    plan = get_object_or_404(TrainingPlan, id=plan_id)
    sessions = TrainingSession.objects.filter(plan=plan)
    return render(request, 'training_plan_sessions.html', {'plan': plan, 'sessions': sessions})

# View to mark a session as completed
@login_required
def mark_session_complete(request, plan_id, session_id):
    session = get_object_or_404(TrainingSession, id=session_id)
    
    # Mark the session as completed
    session.completed = True
    session.save()

    # Update the training plan progress
    plan = session.plan
    total_sessions = plan.sessions.count()
    completed_sessions = plan.sessions.filter(completed=True).count()
    
    # Update progress: completed_sessions / total_sessions * 100
    if total_sessions > 0:
        plan.progress = (completed_sessions / total_sessions) * 100
    else:
        plan.progress = 0  # Prevent division by zero if no sessions exist
    
    plan.save()

    # Redirect back to the session list
    return redirect('training_plan_sessions', plan_id=plan.id)

# View to create a new training plan
@login_required
def create_training_plan(request):
    if request.method == "POST":
        # Get data from the form
        name = request.POST.get("name")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        goal = request.POST.get("goal")
        training_type = request.POST.get("training_type")
        training_frequency = int(request.POST.get("training_frequency"))
        notes = request.POST.get("notes")
        
        # Debugging: print the values received from the form
        print(f"Name: {name}, Start Date: {start_date}, End Date: {end_date}, Goal: {goal}")
        print(f"Training Type: {training_type}, Frequency: {training_frequency}, Notes: {notes}")

        # Convert string dates to datetime.date objects
        start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        end_date = datetime.strptime(end_date, "%Y-%m-%d").date()

        # Check if all values are received correctly
        if not name or not start_date or not end_date:
            print("Missing required fields.")
            return render(request, 'create_plan.html', {'error': 'All fields are required.'})

        # Create a new training plan for the logged-in user
        plan = TrainingPlan.objects.create(
            user=request.user,
            name=name,
            start_date=start_date,
            end_date=end_date,
            goal=goal,
            progress=0,  # Initial progress is 0
            notes=notes
        )

        # Automatically create sessions for the plan
        create_sessions_for_plan(plan, training_type, training_frequency)

        # After creating the plan and sessions, redirect to the training plans list
        return redirect('training_plans')  # Name of the view that lists training plans
    
    return render(request, 'create_plan.html')
# View to create a new session for a specific training plan
@login_required
def create_training_session(request, plan_id):
    plan = get_object_or_404(TrainingPlan, id=plan_id)

    if request.method == "POST":
        # Get the data from the form
        day = request.POST.get("day")
        exercises = request.POST.get("exercises")
        target_sets = request.POST.get("target_sets")
        target_reps = request.POST.get("target_reps")
        target_weight = request.POST.get("target_weight")
        
        # Create a new session and associate it with the plan
        session = TrainingSession.objects.create(
            plan=plan,
            day=day,
            exercises=exercises,
            target_sets=target_sets,
            target_reps=target_reps,
            target_weight=target_weight,
        )

        # After creating the session, redirect to the session list for this plan
        return redirect('training_plan_sessions', plan_id=plan.id)

    return render(request, 'create_session.html', {'plan': plan})

# Automatically create sessions when a plan is created (e.g., 4 weeks of training)
def create_sessions_for_plan(plan, training_type, training_frequency):
    # Ensure start_date and end_date are datetime.date objects
    start_date = plan.start_date  # This should already be a datetime.date object in Django
    end_date = plan.end_date  # This should also be a datetime.date object in Django

    # Calculate number of weeks based on start and end date
    num_weeks = (end_date - start_date).days // 7  # Number of weeks between start and end date

    exercises_dict = {
        'strength': ["Squats", "Deadlifts", "Bench Press", "Pull-ups"],
        'endurance': ["Running", "Cycling", "Rowing", "Swimming"],
        'flexibility': ["Yoga", "Stretching", "Pilates"],
        'general': ["Jogging", "Bodyweight Squats", "Push-ups", "Plank"]
    }

    exercises = exercises_dict.get(training_type, exercises_dict['general'])  # Default to 'general' if invalid type
    session_day_names = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7"]

    # Create sessions based on frequency
    for week in range(1, num_weeks + 1):
        for day in range(training_frequency):  # Create sessions based on training frequency
            day_name = session_day_names[day % len(session_day_names)]  # Cycle through the days
            day_label = f"Week {week}, {day_name}"
            exercises_list = ', '.join(exercises)
            target_sets = 4
            target_reps = 12
            target_weight = 50.0  # Example weight for each exercise

            # Calculate the due date based on plan's start_date
            due_date = start_date + timedelta(weeks=week-1, days=day)

            # Create a new session for the plan
            session = TrainingSession.objects.create(
                plan=plan,
                day=day_label,
                exercises=exercises_list,
                target_sets=target_sets,
                target_reps=target_reps,
                target_weight=target_weight,
                completed=False,
                due_date=due_date
            )