from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    return render(request, 'home.html', {})

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        send_mail(
            'Welcome to Vitalog:' + message_name, #email subject
            message,
            message_email, # from or sender's email
            ['community.vitalog@gmail.com'], # email patient is sending to
            fail_silently=False,
        )

        return render(request, 'contact.html', {'message_name': message_name})

    else: 
        #return page
        return render(request, 'contact.html', {})
