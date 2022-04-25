from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment, Profile, News


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ('news', 'user', 'name_user')


class CommentForm2(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ('news', 'user')


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class RegisterProfileForm(forms.ModelForm):
    city = forms.CharField(label='Город проживания', max_length=36, required=False)
    phone = forms.CharField(label='Номер телефона', max_length=15, required=False)

    class Meta:
        model = Profile
        fields = ('city', 'phone')
