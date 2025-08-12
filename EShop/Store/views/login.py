from  django.shortcuts import render,redirect,HttpResponseRedirect
from  Store.models.customer import Customer
from  django.contrib.auth.hashers import check_password
from  django.views import View
from django.core.mail import send_mail
from django.contrib import messages
import random
from Store.tasks import send_otp_email
from django.contrib.auth.hashers import make_password
# from Store.task import * 

class Login(View):
    return_url = None

    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request,'login.html')

    def post(self, request):
        email = request.POST.get('Email') # Email is data base filed Name 
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None

        if customer:
            flag = check_password(password, customer.Password) # Password is data base filed Name 
            if flag:
                request.session['customer'] = customer.id
                request.session['email'] = customer.Email 
                request.session['first_name'] = customer.First_Name

                messages.success(request,"Welcome! you have successfully logged in.")

                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url) # kisi url pe url ki help se redirect karna chahte tab use karenge hum iska Http kaa
                else:
                    Login.return_url = None
                    return redirect('homepage')
            else:
                error_message = 'Email or password invalid!!'
        else:
            error_message = 'Email or password invalid!!'  
                 
        print(customer)
        print(email,password)
        return render(request,'login.html',{'error':error_message})

   
def logout(request):
    messages.info(request, 'You have been logged out successfully.')
    request.session.clear()
    return redirect('login')

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        otp = random.randint(100000, 999999)  # Generate OTP

        # Save OTP to customer record
        customer = Customer.get_customer_by_email(email)
        if customer:
            customer.otp = str(otp)
            customer.save()
           
            #  Send OTP email using Celery task
            send_otp_email(email, otp, customer.First_Name)

            request.session['email'] = email  # Store email in session
            messages.success(request, 'OTP sent to your email.')
            return redirect('verify_otp')
        else:
            messages.error(request, 'Email not found.')
    return render(request, 'forgot_password.html')

# Verify OTP
def verify_otp(request):
    if request.method == 'POST':
        email = request.session.get('email')
        customer = Customer.get_customer_by_email(email)
        if customer:
            otp_entered = request.POST['otp']
            if otp_entered == customer.otp:
                return redirect('reset_password')  # Redirect to reset password page
            else:
                messages.error(request, 'Invalid OTP')
        else:
            messages.error(request, 'Email not found.')

    return render(request, 'verify_otp.html')

# Resend OTP
def resend_otp(request):
    email = request.session.get('email')
    customer = Customer.get_customer_by_email(email)
    if customer:
        otp = random.randint(100000, 999999)  # Generate OTP
        customer.otp = str(otp)
        customer.save()

        # Send OTP email asynchronously using Celery task
        send_otp_email(email, otp, customer.First_Name)
    
        messages.success(request, 'OTP resent to your email.')
    else:
        messages.error(request, 'Email not found.')

    return redirect('verify_otp')
    
def reset_password(request):
    if request.method == 'POST':
        email = request.session.get('email')
        if email:
            try:
                customer = Customer.objects.get(Email=email)
                password = request.POST.get('password')
                confirm_password = request.POST.get('confirm_password')

                if password == confirm_password:
                    hashed_password = make_password(password)
                    customer.Password = hashed_password
                    customer.save()
                    messages.success(request, 'Password reset successfully. You can now log in.')
                    return redirect('login') # Redirect to login page after reset
                else:
                    messages.error(request, 'Passwords do not match. Please try again.')
            except Customer.DoesNotExist:
                messages.error(request, 'User not found with this email address.')
        else:
            messages.error(request, 'Invalid email. Please try again.')

    return render(request, 'reset_password.html')


