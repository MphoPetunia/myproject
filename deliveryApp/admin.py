from django.contrib import admin
from .models import Customer, Pharmacy, Medicine, Order

# Register your models here.
admin.site.register(Customer)
admin.site.register(Pharmacy)
admin.site.register(Medicine)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display =(
        'id','customer','order_date'
    )


