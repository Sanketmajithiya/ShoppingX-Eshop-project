from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['id', 'Name', 'Price', 'category', 'Image', 'Description']
    list_filter = ('Name', 'Price', 'category')  
    search_fields = ('Name', 'Description')  


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['id', 'Name']  
    search_fields = ('Name',)  


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'First_Name', 'Last_Name', 'Phone', 'Email'] 
    search_fields = ('First_Name', 'Last_Name', 'Email', 'Phone')  


@admin.register(Order)
class OrderModel(admin.ModelAdmin):
    list_display = ['id', 'Product', 'Customer', 'Quantity', 'Price', 'Address', 'Phone', 'Date']
    list_filter = ('Date', 'Product', 'Customer')  
    search_fields = ('Product__Name', 'Customer__Email', 'Address', 'Phone')  














































# @admin.register(Product)
# class AdminProduct(admin.ModelAdmin):
#     list_display = ['id','Name','Price','category','Image','Description']
#     list_filter = ('Name', 'Price')
#     # list_select_related = True
#     search_fields = ('Name',)

# class AdminCategory(admin.ModelAdmin):
#     list_display = ['Name']    

# # Register your models here.


# admin.site.register(Category, AdminCategory)

# @admin.register(Customer)
# class CustomerModelAdmin(admin.ModelAdmin):
#     list_display =['id','First_Name','Last_Name','Phone','Email','Password']

# @admin.register(Order)
# class OrderModel(admin.ModelAdmin):
#     list_display =['id','Product','Customer','Quantity','Price','Address','Phone','Date']