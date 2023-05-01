from django.shortcuts import render, redirect
from .models import Customer, Pharmacy, Medicine, Order
from .forms import CustomerForm

# Create your views here.
def home(request):
    return render(request,'home/home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def services(request):
    return render(request,'services.html')

def customer_list(request):
    customers = Customer.objects.all()
    return render(request,'customer_list.html',{'customers':customers})

def pharmacy_list(request):
    pharmacies = Pharmacy.objects.all()
    return render(request,'pharmacy_list.html',{'pharmacies':pharmacies})

def medicine_list(request):
    medicines = Medicine.objects.all()
    return render(request,'medicine_list.html',{'medicines':medicines})

def order_list(request):
    orders = Order.objects.all()
    return render(request,'order_list.html',{'orders':orders})

def create_customer(request):
    if request.method =='POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
        else:
            form = CustomerForm()

            return render(request,'create_customer.html',{'form':form})


