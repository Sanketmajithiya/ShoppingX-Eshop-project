from django.db import models
from .category import Category

# Create your models here.

class Product(models.Model):
    Name = models.CharField(max_length=50)
    Price = models.IntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, default=1)
    Description = models.CharField(max_length=200, default='',null=True, blank=True)
    Image = models.ImageField(upload_to='uploads/products/')
    

    def __str__(self):
        return self.Name

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)
        
# Data ko get karne

    @staticmethod
    def get_all_products():
        return Product.objects.all()
    
    @staticmethod
    def get_all_products_by_categoryid(Category_id):
        if Category_id:
           return Product.objects.filter(category=int(Category_id))
        else:
            return Product.get_all_products()
