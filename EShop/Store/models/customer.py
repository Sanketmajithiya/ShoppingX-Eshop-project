from django.db import models

class Customer(models.Model):
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Phone = models.CharField(max_length=15)
    Email = models.EmailField()
    Password = models.CharField(max_length=128)
    otp = models.CharField(max_length=6, blank=True, null=True)  

    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):    
        try:
            return Customer.objects.get(Email=email) # Email is data base filed Name 
        except Customer.DoesNotExist:
            return None


    def isExist(self):
        if Customer.objects.filter(email=self.Email):
            return True
        return False    

    def __str__(self):
        return self.First_Name 