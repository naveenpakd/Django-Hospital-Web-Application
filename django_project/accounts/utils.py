

from django.contrib.auth.models import User,auth
from django.core.mail import send_mail

from django.conf import settings 


def send_email_token(email , token ):
    subject = 'Your Email Need Verification'
    message = f'Hi , click on link to verify  http://127.0.0.1:8000/accounts/email/{token}/'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    return True
