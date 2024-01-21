from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm

from . import models
from .utils import *


# Create your views here.

def home(request):
    context = {}
    return render(request, 'myapp/homepage.html', context=context)


# Create your views here.
def register(request):
    context = {}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            dob = request.POST["dob"]
            acct_holder = AccountHolder(
                user=new_user,
                date_of_birth=dob,
            )
            acct_holder.save()

            return HttpResponseRedirect(reverse('login'))
        else:
            # Add error messages to context
            error_messages = form.errors
            context['error_messages'] = error_messages
    else:
        form = UserCreationForm()
    context['form'] = form
    return render(request, 'myapp/register.html', context)

def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('home'))

    context = {}
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                context['error'] = "Invalid username or password."
        else:
            context['form_errors'] = form.errors
    else:
        form = AuthenticationForm(request)

    context['form'] = form
    return render(request, 'myapp/login.html', context)



def compatability_view(request):
    if request.method == 'POST':
        sign_one = request.POST.get('sign1')
        sign_two = request.POST.get('sign2')
        compatability_result = compare_signs(sign_one, sign_two)
        return render(request,
                      "myapp/results.html", context=compatability_result)

