from django import forms
from .models import Customer, Pharmacy, Medicine, Order

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('first_name','last_name','address','phone_number')
        
class PharmacyForm(forms.ModelForm):
    class Meta:
        model = Pharmacy
        fields = ('name','phone_number','address')
        
class MedicineForm(forms.ModelForm):
    class Meta:
        model: Medicine  
        fields = ('name','description','price')   
        
class OrderForm(forms.ModelForm):
    class Meta:
        model: Order
        fields =('customer','pharamacy','medicine','order_date')       

