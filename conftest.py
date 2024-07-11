# conftest.py

import pytest
from django.conf import settings
ROOT_URLCONF = 'celeryproject.urls'
# Ensure Django settings are configured
settings.configure(
    DEBUG=True,
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:'
        }
    },
    INSTALLED_APPS=[
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'celeryproject',  
    ],
)

# Initialize Django
import django
django.setup()
