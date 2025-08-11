from  django.shortcuts import render,redirect
from  Store.models.customer import Customer
from  django.views import View
from Store.models.product import Product
from Store.models.orders import Order
from django.http import HttpResponse
import razorpay
from django.conf import settings
import time
from razorpay.errors import BadRequestError  # Import the correct error class
from razorpay.errors import SignatureVerificationError

razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

class CheckOut(View):
    def get(self, request):
        # Handle GET request for checkout
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        
        if not customer or not cart:
            return redirect('cart')  # Redirect to cart if no cart or customer session
        
        products = Product.get_products_by_id(list(cart.keys()))
        total_amount = sum(product.Price * cart.get(str(product.id)) for product in products)

        return render(request, 'checkout.html', {
            'total_amount': total_amount,
            'products': products
        })

    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))

        if not address or not phone:
            return HttpResponse("Address and phone number are required.", status=400)

        # Save address and phone in session
        request.session['checkout_details'] = {'address': address, 'phone': phone}

        total_amount = sum(product.Price * cart.get(str(product.id)) for product in products)
        total_amount_paise = total_amount * 100  # Convert to paise
    
        try:
            razorpay_order = razorpay_client.order.create({
                "amount": total_amount_paise,
                "currency": "INR",
                "receipt": f"order_{customer}_{int(time.time())}",
                "payment_capture": 1,
            })
            request.session['razorpay_order_id'] = razorpay_order['id']

            return render(request, 'checkout.html', {
                'razorpay_order_id': razorpay_order['id'],
                'razorpay_amount': total_amount_paise,
                'razorpay_key': settings.RAZORPAY_KEY_ID,
                'products': products,
                'total_amount': total_amount,
            })
        except BadRequestError as e:
            return HttpResponse(f"Error: {str(e)}", status=500)

class PaymentSuccess(View):
    def get(self, request):
        # Razorpay order id aur payment id ko session mein store karna
        razorpay_order_id = request.session.get('razorpay_order_id')
        razorpay_payment_id = request.session.get('razorpay_payment_id')

        # Agar session mein payment information nahi hai
        if not razorpay_order_id or not razorpay_payment_id:
            return HttpResponse("Payment information is missing.", status=400)

        # Checkout details aur customer info ko retrieve karna
        checkout_details = request.session.get('checkout_details', {})
        address = checkout_details.get('address')
        phone = checkout_details.get('phone')
        customer_id = request.session.get('customer')
        cart = request.session.get('cart')

        if not address or not phone or not cart or not customer_id:
            return HttpResponse("Required session data is missing.", status=400)

        try:
            # Customer aur unke products ko fetch karna
            customer = Customer.objects.get(id=customer_id)
            products = Product.get_products_by_id(list(cart.keys()))
            total_amount = sum(product.Price * cart.get(str(product.id)) for product in products)

            # Success page ke liye context prepare karna
            context = {
                'user_FirstName': customer.First_Name,
                'user_LastName': customer.Last_Name,
                'product_Name': ', '.join([product.Name for product in products]),
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': razorpay_payment_id,
                'total_amount': total_amount,
                'payment_status': 'Success',
            }

            return render(request, 'payment-success.html', context)

        except Exception as e:
            return HttpResponse(f"Error occurred: {str(e)}", status=500)


    def post(self, request):
        razorpay_order_id = request.POST.get('razorpay_order_id')
        razorpay_payment_id = request.POST.get('razorpay_payment_id')
        razorpay_signature = request.POST.get('razorpay_signature')

        try:
            # Razorpay payment signature ko verify karna
            razorpay_client.utility.verify_payment_signature({
                "razorpay_order_id": razorpay_order_id,
                "razorpay_payment_id": razorpay_payment_id,
                "razorpay_signature": razorpay_signature,
            })

            # Session data ko retrieve karna
            checkout_details = request.session.get('checkout_details', {})
            address = checkout_details.get('address')
            phone = checkout_details.get('phone')
            customer_id = request.session.get('customer')
            cart = request.session.get('cart')

            if not address or not phone or not cart or not customer_id:
                return HttpResponse("Required session data is missing.", status=400)

            # Customer aur products fetch karna
            customer = Customer.objects.get(id=customer_id)
            products = Product.get_products_by_id(list(cart.keys()))
            total_amount = sum(product.Price * cart.get(str(product.id)) for product in products)

            # Orders create karna
            for product in products:
                Order.objects.create(
                    Customer=customer,
                    Product=product,
                    Price=product.Price,
                    Address=address,
                    Phone=phone,
                    Quantity=cart.get(str(product.id)),
                )

            # Session ko clear karna
            request.session['cart'] = {}
            request.session.pop('razorpay_order_id', None)
            request.session.pop('checkout_details', None)

            # Payment success ke liye context banana
            context = {
                'user_FirstName': customer.First_Name,
                'user_LastName': customer.Last_Name,
                'product_Name': ', '.join([product.Name for product in products]),
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': razorpay_payment_id,
                'total_amount': total_amount,
                'payment_status': 'Success',
            }

            return render(request, 'payment-success.html', context)

        except razorpay.errors.SignatureVerificationError:
            return HttpResponse("Payment verification failed", status=400)
        except Exception as e:
            return HttpResponse(f"Error: {str(e)}", status=500)


# class PaymentSuccess(View):
#     def post(self, request):
#         razorpay_order_id = request.POST.get('razorpay_order_id')
#         razorpay_payment_id = request.POST.get('razorpay_payment_id')
#         razorpay_signature = request.POST.get('razorpay_signature')

#         try:
#             # Verify payment signature
#             razorpay_client.utility.verify_payment_signature({
#                 "razorpay_order_id": razorpay_order_id,
#                 "razorpay_payment_id": razorpay_payment_id,
#                 "razorpay_signature": razorpay_signature,
#             })
#             # Retrieve session data
#             checkout_details = request.session.get('checkout_details', {})
#             address = checkout_details.get('address')
#             phone = checkout_details.get('phone')
#             customer_id = request.session.get('customer')
#             cart = request.session.get('cart')

#             if not address or not phone or not cart or not customer_id:
#                 return HttpResponse("Required session data is missing.", status=400)

#             customer = Customer.objects.get(id=customer_id)
#             user_name = f"{customer.First_Name} {customer.Last_Name}"

#             products = Product.get_products_by_id(list(cart.keys()))
#             total_amount = sum(product.Price * cart.get(str(product.id)) for product in products)

#             for product in products:
#                 Order.objects.create(
#                     Customer=customer,
#                     Product=product,
#                     Price=product.Price,
#                     Address=address,
#                     Phone=phone,
#                     Quantity=cart.get(str(product.id)),
#                 )
#             # Clear session data
#             request.session['cart'] = {}
#             request.session.pop('razorpay_order_id', None)
#             request.session.pop('checkout_details', None)

#             context = {
#                 'user_FirstName': customer.First_Name,
#                 'user_LastName': customer.Last_Name,
#                 'product_Name': ', '.join([product.Name for product in products]),
#                 'razorpay_order_id': razorpay_order_id,
#                 'razorpay_payment_id': razorpay_payment_id,
#                 'total_amount': total_amount,
#                 'payment_status': 'Success',
#             }

#             return render(request, 'payment-success.html', context)

#         except razorpay.errors.SignatureVerificationError:
#             return HttpResponse("Payment verification failed", status=400)
#         except Exception as e:
#             return render(request, 'payment-success.html', context)
        

#         except razorpay.errors.SignatureVerificationError:
#             return HttpResponse("Payment verification failed.", status=400)
#         except Exception as e:
#             return HttpResponse(f"Error: {str(e)}", status=500)






























# class CheckOut(View):
#     def post(self, request):
#         address = request.POST.get('address')
#         phone = request.POST.get('phone')
#         customer = request.session.get('customer')
#         cart = request.session.get('cart')
#         products = Product.get_products_by_id(list(cart.keys()))
#         print(address,phone,customer,cart,products)

#         for product in products:
#             print(cart.get(str(product.id)))
#             order = Order(
#                 Customer = Customer(id=customer),
#                 Product = product,
#                 Price = product.Price,
#                 Address = address,
#                 Phone = phone,
#                 Quantity = cart.get(str(product.id)),
#             )
#             order.save()
#             request.session['cart'] = {} # After checkout cart will be Empty

#             return redirect('cart')