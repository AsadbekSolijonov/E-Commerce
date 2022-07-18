from django.contrib import admin
from store.models import Customer, Order, OrderItem, ShippingAdress, Product

# Register your models here.

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAdress)
admin.site.register(Product)
