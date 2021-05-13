from django.shortcuts import render
from .models import appointment
from django.core.mail import send_mail
from django.contrib.auth.models import User, Group
from django.conf import settings


# Create your views here.
def index(request):

    data='none'

    if request.method=='POST':
        Name=request.POST['Name']
        Email=request.POST['Email']
        select_Date=request.POST['select_Date']
        select_Department = request.POST['select_Department']
        Phone_Number=request.POST['Phone_Number']
        Additional_Message=request.POST['Additional_Message']
        data=appointment.objects.create(Name=Name, Email= Email,select_Date=select_Date,select_Department=select_Department,Phone_Number=Phone_Number,Additional_Message=Additional_Message)
        user = User.objects.create_user(email=Email,username=Name)
        user.save()
        data.save()

        # send an email

        subject = 'Welcome to Health center Hospital' \

        message = f'Hi' \
                  f' {data.Name},' \
                  f' thank you for booking slot.' \
                  f' your slot will be held on {data.select_Date} at 10:30 A.M on {data.select_Department}.' \
                  f' Note : once the slot is booked , cannot be cancelled or changed the slot. '  \
                  f' Follow the below link for map :https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3647.3030413476204!2d100.5641230193719!3d13.757206847615207!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0xf51ce6427b7918fc!2sG+Tower!5e0!3m2!1sen!2sth!4v1510722015945'






        email_from = settings.EMAIL_HOST_USER
        recipient_list = [data.Email, ]
        send_mail(subject, message, email_from, recipient_list)

        return render(request, 'done.html',{
            'data': data
        })


    else:

        return render(request ,'index.html',{})



def done(request):
    return render(request , 'done.html')















