from django.contrib import admin
from django.contrib.auth.models import User

# Register the User model so it shows up in the admin interface
admin.site.register(User)
