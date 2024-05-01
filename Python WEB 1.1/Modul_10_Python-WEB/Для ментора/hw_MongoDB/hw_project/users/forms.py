from quotes.models import Author, Quote
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import CustomUser

class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput())

    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2']



class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('fullname', 'born_date', 'born_location', 'description')


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ('quote', 'tags', 'author')
