from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import event_scheduler
from . forms import EventSchedulerForm
from send_mail_app.tasks import send_mail_func
from datetime import timedelta,datetime
from django.utils import timezone

          
def index(request): # Home page of application
    return render(request, 'index.html')

def add(request): # Allows user to enter event details, doent allow previous date and all fields are mendatory
    x = event_scheduler.objects.all()
    if request.method == 'POST':
        i=request.POST['quantity']
        name = request.POST['eventname']
        date = request.POST['birthday']
        time = request.POST['appt']
        description = request.POST['message']
        event_type=request.POST['event_type']
        user_mail=request.POST['email']
        d = datetime.strptime(date, "%Y-%m-%d").date() #extract string into date object, and extract date part 
        t = datetime.strptime(time, "%H:%M").time()
        if d < timezone.now().date(): # check date is in past or future, if past ten it will not save event to database
            return HttpResponse("data is previous")
        
        new_event = event_scheduler(i=i,name=name, date=date, time=time, description=description, event_type=event_type,user_mail=user_mail)
        new_event.save()
        try:
            send_mail_func(user_mail,name,date,time) #call sendMail function for mail scheduling 
            reminder_date = d - timedelta(days=1)
            reminder_time = datetime.combine(reminder_date, t)
            print(reminder_time)
            send_mail_func.apply_async((user_mail, name, date, time), eta=reminder_time)
            print("success")
        except Exception as e:
            print("Error------")
            print(e)
        return redirect('display')
    return render(request, 'add.html')

def display(request): #display event details, sorted by date and time
    if request.method == 'POST':
        i=request.POST['quantity']
        name = request.POST['eventname']
        date = request.POST['birthday']
        time = request.POST['appt']
        description = request.POST['message']
        obj=event_scheduler(i=i)
        obj.i=i
        obj.name=name
        obj.date=date
        obj.time=time
        obj.description=description
        obj.save()
    from django.core import serializers # convert python script to json like format
    data = serializers.serialize("python",event_scheduler.objects.all())
    context = {
        'data': data,
    }
    
    return render(request, 'display.html',context)

def display_filter(request): # filter data by id, if we give input then it will display all events related to that id
    if request.method == 'POST':
        event_id = request.POST.get('quantity')
        events = event_scheduler.objects.filter(i=event_id)
        return render(request, 'display_filter.html', {'events': events})
    return render(request, 'input.html')

def delete(request): #delete event by id
    if request.method == 'POST':
        event_id = request.POST.get('id') #fetch event id
        events = event_scheduler.objects.filter(i=event_id) #filter events by id
        if events.exists(): #check id exists in datbase or not
            events.delete()
            return HttpResponse("Data deleted")
        else:
            return HttpResponse("Data Not found")
    return render(request, 'delete.html')

def update(request): #update existing event details by id
    if request.method == 'POST':
        event_id = request.POST.get('quantity') #take event id from user
        events = event_scheduler.objects.filter(i=event_id) #filter events by id
        if events.exists(): #check id exist or not
            event = events.first()  
            event.name = request.POST.get('eventname')
            event.date = request.POST.get('birthday')
            event.time = request.POST.get('appt')
            event.description = request.POST.get('message')
            event.event_type=request.POST['event_type']
            event.user_mail=request.POST['email']
            event.save()
            return HttpResponse("Data Updated")
        else:
            return HttpResponse("Data Not Found")
    
    return render(request, 'update.html')


def remediation(request): #remediation task, put all None value cells of user email to default email
    events = event_scheduler.objects.all()
    if request.method == 'POST':
        i=request.POST['quantity']
        name = request.POST['eventname']
        date = request.POST['birthday']
        time = request.POST['appt']
        description = request.POST['message']
        obj=event_scheduler(i=i)
        obj.i=i
        obj.name=name
        obj.date=date
        obj.time=time
        obj.description=description
        obj.save()
    from django.core import serializers
    events = serializers.serialize("python",event_scheduler.objects.all())
    context = {
        'events': events,
    }
    return render(request, 'remediation.html', {'events': events})



