from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ClearableFileInput
from .models import Comment, Profile
from django.utils.translation import gettext_lazy as _


class PostPhotoForm(forms.Form):
    text = forms.CharField(label=_('Текст'))
    image = forms.ImageField(label=_('Фотографии'), widget=ClearableFileInput(attrs={'multiple': True}))


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ('post', 'user', 'name_user')


class CommentForm2(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ('post', 'user')


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label=_('Логин'), widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label=_('Пароль'), widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label=_('Повтор пароля'), widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    first_name = forms.CharField(label=_('Имя'), widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(label=_('Фамилия'), widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name')


class RegisterProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('city', 'phone', 'avatar')


class UploadPostForm(forms.Form):
    file = forms.FileField()