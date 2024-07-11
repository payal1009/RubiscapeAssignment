from django.contrib.auth import get_user_model

from celery import shared_task
from django.core.mail import send_mail
from celeryproject import settings

@shared_task(bind=True)
def send_mail_func(self,user_mail,name,date,time):    
        print(date,time)
        try:
            print(user_mail,name,date)
            mail_subject = f"Hello: {name} "
            message = f"Good Morning '{name}' date '{date} at '{time}'"
            #to_email = user.email
            send_mail(
                subject = mail_subject,
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user_mail],
                fail_silently=True,
            )
            print("*****")
        except Exception as e:
            print("Error")
            print(e)
        return "Done"
