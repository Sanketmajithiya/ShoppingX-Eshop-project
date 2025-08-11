from Store.models import *
import time
from django.core.mail import send_mail,EmailMessage # ye class hoti hai hamare pass
from django.conf import settings



def send_email_to_client():
    subject ="This Email is from Django server"
    message = "This is a test message from Django server email"
    from_email =  settings.EMAIL_HOST_USER
    recipint_list = ["sanketmajithiya@gmail.com"] # App kis-kis  ko behj naa cahte ho
    send_mail(subject, message, from_email, recipint_list)


def send_email_with_attachment(subject, message, recipint_list, file_path):
    mail = EmailMessage(subject=subject, body = message, from_email=settings.EMAIL_HOST_USER, to = recipint_list)

    mail.attach_file(file_path)
    mail.send()

