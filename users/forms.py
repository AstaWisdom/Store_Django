from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import BuySpecial


class UserForm(UserCreationForm):
    trading_link = forms.CharField(max_length=255)
    username = forms.CharField(max_length=30, min_length=1, help_text='* at least 1 characters')
    email = forms.CharField(max_length=200, help_text='example@gmail.com')


    class Meta:
        model = User
        fields = ['username', 'email', 'trading_link']


class SpecialBuyForm(forms.ModelForm):
    class Meta:
        model = BuySpecial
        fields = ['name', 'email', 'phone_number', 'text']
