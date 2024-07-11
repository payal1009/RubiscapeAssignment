from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

def validate_future_date(value):
    if value < timezone.now().date():
        raise ValidationError('Event date cannot be in the past.')
    
class event_scheduler(models.Model):
    i=models.IntegerField()
    #eventNo = models.IntegerField(unique=True,editable=False)
    name = models.TextField()
    date = models.DateField(validators=[validate_future_date])
    time = models.TimeField()
    description = models.TextField()
    event_type=models.TextField(null=True)
    user_mail=models.EmailField(null=True)
    def __str__(self):
        return f"{self.i},{self.name},{self.date},{self.time},{self.description},{self.event_type},{self.user_mail}"
    
    class Meta:
        ordering = ['date', 'time','i'] # sort events by date, time and id
      
