# views.py
from django.shortcuts import render, redirect
from .forms import BodyDataForm
from .models import BodyData
from django.contrib.auth.decorators import login_required

@login_required
def add_body_data(request):
    if request.method == 'POST':
        form = BodyDataForm(request.POST)
        if form.is_valid():
            body_data = form.save(commit=False)
            body_data.user = request.user  # Associate with the logged-in user
            body_data.save()
            return redirect('body_data')  # Redirect to body data page
    else:
        form = BodyDataForm()
    
    return render(request, 'addbody.html', {'form': form})

@login_required
def body_data(request):
    records = BodyData.objects.filter(user=request.user).order_by('-date')
    return render(request, 'body_data.html', {'records': records})
