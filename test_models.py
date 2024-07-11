import pytest
from django.core.exceptions import ValidationError
from django.utils import timezone
from celeryproject.models import event_scheduler

@pytest.mark.django_db
def test_create_event():
    event = event_scheduler.objects.create(
        i=1,
        name='Test Event',
        date=timezone.now().date() + timezone.timedelta(days=1),
        time='12:00',
        description='Test Description',
        event_type='Conference',
        user_mail='test@example.com'
    )
    assert event.id is not None

