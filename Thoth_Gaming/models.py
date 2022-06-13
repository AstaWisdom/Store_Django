from django.db import models
from django.contrib.auth.models import User
from items.models import Item
from users.models import Customer, UserDashboard


# Create your models here.
class Order(models.Model):
    complete = models.BooleanField(default=False, blank=False, null=False)
    trade_link = models.CharField(max_length=255, blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return f"user: {self.user} || order_id: {str(self.id)}"

    @property
    def cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.total for item in orderitems])

        if self.user.userdashboard.get_invite_friends >= 5:
            total = total - (total * (5/100))

        return total

    @property
    def cart_total_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])

        return total


class OrderItem(models.Model):
    items = models.ForeignKey(Item, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return str(self.order)

    @property
    def total(self):
        total = self.items.price * self.quantity
        return total


class Payment(models.Model):
    status = models.IntegerField()
    track_id = models.IntegerField()
    id_number = models.CharField(max_length=100)
    oder_id = models.CharField(max_length=200)
    amount = models.IntegerField()
    card_number = models.CharField(max_length=200)
    hash_card_number = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)