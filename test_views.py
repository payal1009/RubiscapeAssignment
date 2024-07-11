import pytest
from django.urls import reverse
from django.test import Client
from django.conf import settings
from django.utils import timezone
from datetime import datetime, timedelta
from celeryproject.settings import ROOT_URLCONF
@pytest.mark.django_db
def test_add_event_view():
    client = Client()
    
    # Ensure settings are accessed correctly
    assert hasattr(settings, 'ROOT_URLCONF'), "ROOT_URLCONF not found in settings"
    assert hasattr(settings, 'EMAIL_HOST_USER')
    # Sample data for the event
    event_data = {
        'quantity': 1,
        'eventname': 'Test Event',
        'birthday': (timezone.now() + timedelta(days=2)).strftime('%Y-%m-%d'),
        'appt': '10:00',
        'message': 'This is a test event',
        'event_type': 'Test',
        'email': 'test@example.com'
    }
    
    response = client.post(reverse('add'), data=event_data)
    
    assert response.status_code == 302  