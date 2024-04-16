from django.shortcuts import render, redirect
from .forms import RegistrationForm, AuthorForm, QuoteForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout


def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Перенаправлення на домашню сторінку після реєстрації
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Перенаправлення на домашню сторінку після входу
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect('http://127.0.0.1:8000/')


def add_author_view(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Перенаправлення на домашню сторінку після додавання автора
    else:
        form = AuthorForm()
    return render(request, 'add_author.html', {'form': form})


def add_quote_view(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Перенаправлення на домашню сторінку після додавання цитати
    else:
        form = QuoteForm()
    return render(request, 'add_quote.html', {'form': form})
