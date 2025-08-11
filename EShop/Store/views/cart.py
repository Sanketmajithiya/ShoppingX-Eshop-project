from django.shortcuts import render
from django.views import View
from Store.models.product import Product
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import razorpay
import json

class Cart(View):
    def get(self, request):
        if 'cart' not in request.session:
            request.session['cart'] = {}

        cart = request.session.get('cart')
        if not cart:
            return render(request, 'cart.html',{'products': [], 'message': "Your cart is empty!"})
        
        ids = list(cart.keys())
        products = Product.get_products_by_id(ids)        
        return render(request, 'cart.html', {'products': products})

@csrf_exempt
def update_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = str(data.get('product_id'))
        quantity = int(data.get('quantity'))

        cart = request.session.get('cart', {})
        if product_id in cart:
            cart[product_id] = quantity
        else:
            cart[product_id] = quantity
        request.session['cart'] = cart
        return JsonResponse({'message': 'Cart updated'})
    return JsonResponse({'error': 'Invalid method'}, status=400)


@csrf_exempt
def remove_from_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = str(data.get('product_id'))

        cart = request.session.get('cart', {})
        if product_id in cart:
            del cart[product_id]
        request.session['cart'] = cart
        return JsonResponse({'message': 'Product removed'})
    return JsonResponse({'error': 'Invalid method'}, status=400) 






































# from  django.shortcuts import render,redirect
# from  Store.models.customer import Customer
# from  django.contrib.auth.hashers import check_password
# from  django.views import View
# from Store.models.product import Product


# class Cart(View):
#     def get(self, request):
#         ids = list(request.session.get('cart').keys())
#         products = Product.get_products_by_id(ids)
#         print(products)
#         # print(list(request.session.get('cart').keys()))
#         return render(request,'cart.html',{'products':products})

