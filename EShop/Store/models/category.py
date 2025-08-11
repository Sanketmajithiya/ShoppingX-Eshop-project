from django.db import models

class Category(models.Model):
    Name = models.CharField(max_length=100)


    def __str__(self):
        return  self.Name

    @staticmethod
    def get_all_categories():
        return Category.objects.all()
    
    @staticmethod
    def get_category_by_name(name):
        return Category.objects.filter(Name=name).first() 
