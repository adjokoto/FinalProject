from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class AccountHolder(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    date_of_birth = models.DateField()


class ZodiacSign(models.Model):
    sign = models.CharField(max_length=20)
    short_name = models.CharField(max_length=3)

    def __str__(self):
        return f'{self.sign} - {self.short_name}'


class Components(models.Model):
    element = models.CharField(max_length=15)
    polarity = models.CharField(max_length=15)
    modality = models.CharField(max_length=15)
    ruling_planet_one = models.CharField(max_length=15)
    ruling_planet_two = models.CharField(max_length=15)
    zodiac_sign = models.ForeignKey(
        ZodiacSign,
        on_delete=models.CASCADE,
    )

    # Class variable to store the count of component fields
    COMPONENT_FIELDS_COUNT = 4

class Traits(models.Model):
    empathy = models.FloatField(default=0)
    resilience = models.FloatField(default=0)
    integrity = models.FloatField(default=0)
    adaptability = models.FloatField(default=0)
    open_mindedness = models.FloatField(default=0)
    responsibility = models.FloatField(default=0)
    confidence = models.FloatField(default=0)
    perseverance = models.FloatField(default=0)
    kindness = models.FloatField(default=0)
    curiosity = models.FloatField(default=0)
    loyalty = models.FloatField(default=0)
    zodiac_sign = models.ForeignKey(
        ZodiacSign,
        on_delete=models.CASCADE,
    )

    # Class variable to store the count of trait fields
    TRAIT_FIELDS_COUNT = 11