from django.core.mail import send_mail
from django.conf import settings
from .models import Customer 


def send_live_sales_email():
    subject = 'Live Sales Alert!'
    message = 'Our live sales are happening now! Don’t miss out on amazing deals.'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user.Email for user in Customer.objects.all()]
    send_mail(subject, message, from_email, recipient_list)
    return f"Emails sent to {len(recipient_list)} users"



def send_otp_email(email, otp, first_name):
    subject = "Your Password Reset OTP | ShoppingX"
    message = f"""
    Dear {first_name},

    Your OTP for password reset is {otp}. Please do not share it with anyone.
    """
    from_email = settings.EMAIL_HOST_USER
    try:
        send_mail(subject, message, from_email, [email])
        return f"OTP sent to {email}"
    except Exception as e:
        return str(e)