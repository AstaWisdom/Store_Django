from django.db import models
from django.contrib.auth.models import User
from .utils import generate_referral_link
# Create your models here.


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    trading_link = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class UserDashboard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    trading_link = models.CharField(max_length=255, blank=True, null=True)
    invite_link = models.CharField(max_length=16, blank=True)
    invited_users = models.ForeignKey(User, on_delete=models.CASCADE, related_name='invited_users', blank=True, null=True)
    invite_friends = models.IntegerField(default=0)
    is_premium = models.BooleanField(default=False)
    is_super_premium = models.BooleanField(default=False)

    @property
    def get_invite_friends(self):
        qs = UserDashboard.objects.all()
        invite = self.invite_friends

        for user in qs:
            if user.invited_users == self.user:
                invite = invite + 1
                self.user.userdashboard.invite_friends = int(invite)

        return invite

    def save(self, *args, **kwargs):
        if self.invite_link == '':
            code = generate_referral_link()
            self.invite_link = code

        super().save(*args, **kwargs)

    def __str__(self):
        return f'user dashboard: {self.name} || user id: {str(self.user.id)} || dashboard id: {str(self.id)}'

#special orders
class BuySpecial(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)
    phone_number = models.IntegerField(blank=False, null=False)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Name: {self.name}|| Request: {self.text[:100]}|| Date: {self.date}"
