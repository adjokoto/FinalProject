from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm

from . import models
from .utils import *
from django.shortcuts import render
from .forms import ZodiacSignForm
from .models import StrengthWeakness


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



def results(request):
    if request.method == 'POST':
        sign_one = request.POST.get('sign1')
        sign_two = request.POST.get('sign2')
        compatability_result = compare_signs(sign_one, sign_two)
        return render(request,
                      "myapp/results.html", context=compatability_result)

def zodiac_comparison(request):
    # if request.method == 'POST':
    #     # Retrieve values for sign1 and sign2 from the POST parameters
    #     sign_one = request.POST.get('sign1')
    #     sign_two = request.POST.get('sign2')
    #
    #     # Get the corresponding ZodiacSign objects
    #     sign1 = ZodiacSign.objects.get(sign=sign_one)
    #     sign2 = ZodiacSign.objects.get(sign=sign_two)

    sign1 = request.GET.get('sign_one')
    sign2 = request.GET.get('sign_two')

#     # Get the StrengthWeakness objects for each sign
    strengths_weaknesses_sign1 = StrengthWeakness.objects.filter(zodiac_sign__sign=sign1).first()
    strengths_weaknesses_sign2 = StrengthWeakness.objects.filter(zodiac_sign__sign=sign2).first()

    return render(request, 'myapp/zodiac_comparison.html', {
        'sign1': sign1,
        'sign2': sign2,
        'strengths_weaknesses_sign1': strengths_weaknesses_sign1,
        'strengths_weaknesses_sign2': strengths_weaknesses_sign2,
    })
    # else:
    #     form = ZodiacSignForm()

    # return render(request, 'myapp/zodiac_form.html', {'form': form})
