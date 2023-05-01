from django.urls import path
from . import views
from accounts.views import signup, signin


urlpatterns =[
    path('',views.home,name='home'),
    path('signup/',signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('about/',views.about,name= 'about'),
    path('contact',views.contact,name='contact'),
    path('services/',views.services,name='services'),
    path('customers/',views.customer_list,name='customer_list'),
    path('pharmacies/',views.pharmacy_list,name='pharmacy_list'),
    path('medicines/',views.medicine_list,name='medicine_list'),
    path('orders/',views.order_list,name='order_list'),
    
  
]

