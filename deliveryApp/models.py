from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    phone_number= models.CharField(max_length=15)
    
    def __str__(self):
        return f"{self.first_name} - {self.last_name}"

class Pharmacy(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'pharmacy'
        verbose_name_plural = 'pharmacies'
        
class Medicine(models.Model):
    name = models.CharField(max_length=100)  
    description = models.TextField() 
    price = models.DecimalField(max_digits=6,decimal_places=2)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'medicine'
        verbose_name_plural = 'medicine'
        
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    pharmacy = models.ForeignKey(Pharmacy,on_delete=models.CASCADE)
    medicine = models.ManyToManyField(Medicine)  
    order_date = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return f"Order#{self.id}"    
    
        
