# test_settings.py

from celeryproject.settings import *  # Import all settings from the main settings file

# Override any necessary settings for tests
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
CELERY_TASK_ALWAYS_EAGER = True
CELERY_TASK_EAGER_PROPAGATES = True

# Ensure these settings are present
ROOT_URLCONF = 'celeryproject.urls'  # Replace 'your_project' with your actual project name
