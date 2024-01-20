from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse

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
    context = dict()
    form = UserCreationForm(request.POST)
    if form.is_valid():
        new_user = form.save()
        print(request)
        dob = request.POST["dob"]
        print("dob")
        print(dob)
        acct_holder = AccountHolder(
            user=new_user,
            date_of_birth=dob,
        )
        acct_holder.save()
        return HttpResponseRedirect(reverse('home'))
    else:
        form = UserCreationForm()
        context['form'] = form
        return render(
            request,
            "myapp/register.html",
            context,
        )


def compatability_view(request):
    if request.method == 'POST':
        sign_one = request.POST.get('sign1')
        sign_two = request.POST.get('sign2')
        compatability_result = compare_signs(sign_one, sign_two)
        return render(request,
                      "myapp/results.html", context=compatability_result)


# def trait_compat_view(request):
#     if request.method == 'POST':
#         sign_one = request.POST.get('sign1')
#         sign_two = request.POST.get('sign2')
#         trait_result = compare_sign_traits(sign_one, sign_two)
#         return render(request,
#                       "myapp/results.html", context=trait_result)


# views.py


# views.py


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
    print(sign1, sign2)

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
