from django.contrib import admin
from .models import Order, OrderItem
from items.models import Item
# Register your models here.
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(OrderItem)