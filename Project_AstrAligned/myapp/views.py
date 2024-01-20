from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages

from . import models
from .utils import *


# Create your views here.

def home(request):
    context = {}
    return render(request, 'myapp/homepage.html', context=context)


# Create your views here.
def register(request):
    context = dict()
    form = UserCreationForm(request.POST)
    error_messages = {}
    if form.is_valid():
        new_user = form.save()
        dob = request.POST["dob"]
        acct_holder = AccountHolder(
            user=new_user,
            date_of_birth=dob,
        )
        acct_holder.save()
        return HttpResponseRedirect(reverse('home'))
    else:
        form = UserCreationForm()
        context['form'] = form
        for field, errors, in form.errors.items():
            # error_messages[field] = error
            # messages.error(request, f"{field}: {error}")
            error_messages[field] = errors
        messages.error(request, 'Error in user registration. Please check the form details and try again!')
        return render(
            request,
            "myapp/register.html",
            {"form": form, "error_messages": error_messages}
            # context,
        )


def compatability_view(request):
    if request.method == 'POST':
        sign_one = request.POST.get('sign1')
        sign_two = request.POST.get('sign2')
        compatability_result = compare_signs(sign_one, sign_two)
        return render(request,
                      "myapp/results.html", context=compatability_result)

