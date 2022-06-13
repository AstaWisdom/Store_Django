from .models import Order
from django import forms


class OrderForm(forms.ModelForm):
    email = forms.EmailField(help_text='توجه داشته باشید برای پیگیری ایمیل شما لازم است')
    class Meta:
        model = Order
        fields = ['email', 'trade_link']


