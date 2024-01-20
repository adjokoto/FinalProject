# forms.py
from django import forms
from .models import ZodiacSign


class ZodiacSignForm(forms.Form):
    sign1 = forms.ModelChoiceField(queryset=ZodiacSign.objects.all(), label='Zodiac Sign 1')
    sign2 = forms.ModelChoiceField(queryset=ZodiacSign.objects.all(), label='Zodiac Sign 2')
