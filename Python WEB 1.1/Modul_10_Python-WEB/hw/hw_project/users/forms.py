from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from quotes.models import Author, Quote


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('fullname', 'born_date', 'born_location', 'description')


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ('quote', 'tags', 'author')
