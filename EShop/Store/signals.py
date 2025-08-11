from django.db.models.signals import post_save,post_delete
from django.core.mail import send_mail
from .models import Order
from django.conf import settings
from django.core.cache import cache
from Store.models.product import Product
from django.dispatch import receiver
from Store.models.category import Category

@receiver(post_save, sender=Order)
def send_order_confirmation_email(sender, instance, created, **kwargs):
    if created:
        customer = instance.Customer  # Use correct field name
        order_id = instance.id
        product = instance.Product
        total_amount = instance.Price * instance.Quantity

        # Prepare email content
        email_subject = 'Your Order Confirmation | ShoppingX'
        email_message = f"""
        Dear {customer.First_Name},

        Thank you for your order! Here are the details:

        Order ID: {order_id}
        Product: {product.Name}
        Quantity: {instance.Quantity}
        Total Amount: {total_amount}

        We will notify you once your order is shipped.

        Best regards,
        ShoppingX Team
        """

        send_mail(
            email_subject,
            email_message,
            settings.DEFAULT_FROM_EMAIL,
            [customer.Email],
        )


@receiver(post_save, sender=Product)# Signal to product cache 
@receiver(post_delete, sender=Product)
def invalidate_product_cache(sender, instance, **kwargs):
    try:
        product_cache_key = f'product_{instance.id}'
        cache.delete(product_cache_key)
        cache.delete(f'category_{instance.Category.id}')  
        cache.delete('home_products')

        print(f"Cache for product {instance.id} invalidated")
    except Exception as e:
        print(f"Error while invalidating product cache: {e}")


@receiver(post_save, sender=Category) # Signal to category cache 
@receiver(post_delete, sender=Category)
def invalidate_category_cache(sender, instance, **kwargs):
    try:
        category_cache_key = f'category_{instance.id}'
        cache.delete(category_cache_key)
        cache.delete('categories')  
        print(f"Cache for category {instance.id} invalidated")
    except Exception as e:
        print(f"Error while invalidating category cache: {e}")