from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class SignUpForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "full_name", "email", "password1", "password2")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 != password2:
            raise ValidationError("Passwords do not match.")
        return password2

class LoginForm(AuthenticationForm):
    # You can add custom validations here if needed
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Your Password'}))

    class Meta:
        model = User
        fields = ("username", "password")
