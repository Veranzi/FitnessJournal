"""
Production settings for fitness_journal project.
"""
import os
import dj_database_url
from .settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-8v=04r(5#1t7s!d=uq#tltvy$cjp-0hx72jjb3da%8ml6f&#%j')

# Update allowed hosts for production
ALLOWED_HOSTS = ['fitnessjournalgain.onrender.com', '.onrender.com', 'localhost', '127.0.0.1']

# Trust the Render domain for CSRF (scheme required)
CSRF_TRUSTED_ORIGINS = [
    'https://fitnessjournalgain.onrender.com',
    'https://*.onrender.com',
]

# Honor X-Forwarded-Proto header set by the proxy (e.g., Render)
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Database configuration for production
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600,
        conn_health_checks=True,
    )
}

# Static files configuration for production
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Add whitenoise middleware for static files
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

# Configure whitenoise
# Keep original filenames to avoid 404s when templates reference non-hashed assets
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# Security settings for production
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# HTTPS settings (uncomment when you have SSL)
# SECURE_SSL_REDIRECT = True
# SECURE_HSTS_SECONDS = 31536000
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True