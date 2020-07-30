from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse


# Create your views here.

#Notifier model --> users cn create multiple notifiers with setting subject, body and recipient of email
## Create notifier id for every notifier

def sendmail(request):

    notifier_id = request.GET['notifier_id']

    ###Use notifier_id to get all notifer details

    send_mail(
        subject = 'That’s your subject', #Get from notifier model
        message = 'That’s your message body Here you can add anything!!!!!!', #Get from notifier model
        from_email = 'progressboardtanish@gmail.com',
        recipient_list = ['tycoonhawk98@gmail.com',],
        # auth_user = 'Login'
        # auth_password = 'Password'
        fail_silently = False,
    )


    responseData = {
        'notifier_id': notifier_id,
        'status' : 'success'
    }


    return JsonResponse(responseData)
