# views.py

from django.shortcuts import render, redirect
from .forms import SleepRecordForm
from .models import SleepRecord
from django.contrib.auth.decorators import login_required

@login_required
def add_sleep_record(request):
    if request.method == 'POST':
        form = SleepRecordForm(request.POST)
        if form.is_valid():
            sleep_record = form.save(commit=False)
            sleep_record.user = request.user  # Associate the sleep record with the logged-in user
            sleep_record.save()
            return redirect('sleep_records')  # Redirect to the sleep records page
    else:
        form = SleepRecordForm()
    
    return render(request, 'addsleep.html', {'form': form})

@login_required
def sleep_records(request):
    records = SleepRecord.objects.filter(user=request.user).order_by('-date')
    return render(request, 'sleeprecords.html', {'records': records})
