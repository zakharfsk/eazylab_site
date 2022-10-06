from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect
from loguru import logger
from django.contrib.auth.forms import AuthenticationForm

from account.forms import SignUpForm
from .models import ProfileUser


# Create your views here.

@logger.catch
def login_page(request: WSGIRequest) -> HttpResponse:
    context = {
        'title': 'Логін',
        'error': '',
    }

    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        logger.info(f'Log In Form: {form.is_valid()}')
        logger.info(f'Log In Form Errors: {form.errors}')
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None and not request.user.is_authenticated:
                login(request, user)
                return redirect('home')
        else:
            for msg in form.errors:
                context['error'] += form.errors[msg]

    return render(request, 'account/login.html', context)


@logger.catch
def register_page(request: WSGIRequest) -> HttpResponse:
    context = {
        'title': 'Реєстрація',
        'error': '',
    }

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        logger.info(f'Sing Up Form: {form.is_valid()}')
        logger.info(f'Log In Form Errors: {form.errors}')
        profile = ProfileUser()
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)

            profile.user = user
            profile.save()

            login(request, user)
            return redirect('home')
        else:
            for msg in form.errors:
                context['error'] += form.errors[msg]

    return render(request, 'account/register.html', context)


@login_required(login_url='login')
@logger.catch
def account_page(request: WSGIRequest) -> HttpResponse:
    context = {
        'title': 'Account',
    }

    return render(request, 'account/account.html', context)


@login_required(login_url='login')
@logger.catch
def logout_page(request: WSGIRequest) -> HttpResponse:
    if request.user.is_authenticated:
        logout(request)
        return redirect('home')
