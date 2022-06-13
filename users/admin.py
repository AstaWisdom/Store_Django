from django.contrib import admin
from .models import Customer, UserDashboard, BuySpecial
# Register your models here.
admin.site.register(Customer)
admin.site.register(UserDashboard)
admin.site.register(BuySpecial)
