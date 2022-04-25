from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import PersonalInfo, BuyerProduct


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class ReplenishTheBalanceForm(forms.ModelForm):
    balance = forms.IntegerField(label='Пополнить на')

    class Meta:
        model = PersonalInfo
        fields = ('balance',)


class BuyingForm(forms.ModelForm):

    class Meta:
        model = BuyerProduct
        exclude = ('shop', 'title', 'price', 'description', 'buyer', 'in_basket', 'is_bought', 'product')