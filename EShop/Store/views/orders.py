from  django.shortcuts import render
from  django.views import View
from Store.models.orders import Order

class OrderView(View):

    # @method_decorator(auth_middleware)
    def get(self, request):
    #    print('middleware')
       customer = request.session.get('customer')
       orders = Order.get_orders_by_customer(customer)
       print(orders)
       orders = orders.reverse()
       return render(request, 'Orders.html',{'orders':orders})
    
