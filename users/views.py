from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages  # Import messages framework
from django.contrib.auth.views import LoginView
from .forms import SignUpForm
from django.contrib.auth import login, authenticate


# SignUp view
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user
            login(request, user)  # Log the user in after sign-up
            messages.success(request, 'You have successfully registered!')
            return redirect('login')  # Redirect to home or dashboard page
        else:
            # Log form errors if invalid
            print(form.errors)  
    else:
        form = SignUpForm()

    return render(request, "signup.html", {"form": form})


def login_view(request):
    if request.method == 'POST':
        # Handle login form submission
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log the user in if authentication is successful
            login(request, user)
            messages.success(request, 'You are now logged in!')
            return redirect('dashboard')  
        else:
            # If the user is invalid or the credentials don't match
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')
