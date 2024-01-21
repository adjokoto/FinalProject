from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login

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

            # Authenticiate and login user
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)

            return HttpResponseRedirect(reverse('home'))
        else:
            # Add error messages to context
            error_messages = form.errors
            context['error_messages'] = error_messages
    else:
        form = UserCreationForm()
    context['form'] = form
    return render(request, 'myapp/register.html', context)

def compatability_view(request):
    if request.method == 'POST':
        sign_one = request.POST.get('sign1')
        sign_two = request.POST.get('sign2')
        compatability_result = compare_signs(sign_one, sign_two)
        return render(request,
                      "myapp/results.html", context=compatability_result)

