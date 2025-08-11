from  django.shortcuts import render,redirect
from  Store.models.customer import Customer
from  django.contrib.auth.hashers import make_password
from  django.views import View
from django.contrib import messages

class Signup(View):
    def get(self, request):#35
        return render(request, 'signup.html')
    
    def post(self, request):
        POST_data = request.POST
        first_name = POST_data.get('FirstName')
        last_name = POST_data.get('LastName')
        phone = POST_data.get('phone')
        email = POST_data.get('Email')
        password = POST_data.get('password')
        # singup page values hold for singup  page 
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email,
        }
        error_message = None

        customer = Customer(
            First_Name=first_name,
            Last_Name=last_name,
            Phone=phone,
            Email=email,
            Password=password,
        )
        error_message = validate_customer(customer)

        if not error_message:
            customer.Password = make_password(customer.Password)
            customer.register()

            messages.success(request, "Thank you for registering. You can now login.")
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value,
            }
            return render(request, "signup.html", data)


def validate_customer(customer):
    error_message = None
    # Validation
    if not customer.First_Name:
        error_message = "First Name is required!"
    elif len(customer.First_Name) < 4:
        error_message = "First Name must be 4 characters or more."
    elif not customer.Last_Name:
        error_message = "Last Name is required!"
    elif len(customer.Last_Name) < 4:
        error_message = "Last Name must be 4 characters or more."
    elif not customer.Phone:
        error_message = "Phone number is required!"
    elif len(customer.Phone) != 10 or not customer.Phone.isdigit():
        error_message = "Phone number must be 10 digits."
    elif not customer.Email:
        error_message = "Email is required!"
    elif len(customer.Email) < 5:
        error_message = "Email must be 5 characters or more."
    elif not customer.Password:
        error_message = "Password is required!"
    elif len(customer.Password) < 6:
        error_message = "Password must be 6 characters or more."
    elif Customer.objects.filter(Email=customer.Email).exists():
        error_message = "Email address is already registered."
    return error_message

