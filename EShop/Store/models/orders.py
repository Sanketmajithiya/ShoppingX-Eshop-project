from django.db import models
from .product import Product
from .customer import Customer
import datetime

class Order(models.Model):
    Product = models.ForeignKey(Product,on_delete=models.CASCADE)
    Customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    Quantity = models.IntegerField(default=1)
    Price =  models.IntegerField()
    Address = models.CharField(max_length=150,default='', blank=True)
    Phone = models.CharField(max_length=11,default='', blank=True)
    Date = models.DateField(default=datetime.datetime.today)
    

    STATUS_CHOICES = (
            ('Accepted', 'Accepted'),
            ('Packed', 'Packed'),
            ('On The Way', 'On The Way'),
            ('Delivered', 'Delivered'),
            ('Cancelled', 'Cancelled'),
            ('Pending', 'Pending'),
        )
    
    Status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='pending')

    razorpay_order_id = models.CharField(max_length=255, blank=True, null=True)
    razorpay_payment_id = models.CharField(max_length=255, blank=True, null=True)
    razorpay_signature = models.CharField(max_length=255, blank=True, null=True)

    def PlaceOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order .objects.filter(Customer=customer_id).order_by('-Date')
    

    def __str__(self):
       return f"Order #{self.id} - {self.Product.Name} by {self.Customer.First_Name}"