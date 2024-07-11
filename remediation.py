from .models import event_scheduler
from django.shortcuts import render
from django.http import HttpResponse

from .models import event_scheduler
def update_emails(request):
    default_email = "default@example.com"
    events = event_scheduler.objects.all()

    for event in events:
        if event.user_mail is None:
            event.user_mail = default_email
            event.save()
            #return HttpResponse("Done")
        else:
            pass
    return HttpResponse("Already Done")
