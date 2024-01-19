from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from . import models


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
        dob = request.POST('dob')
        acct_holder = models.AccountHolder(
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


