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
    ruling_house_one = models.CharField(max_length=15)
    ruling_house_two = models.CharField(max_length=15)
    zodiac_sign = models.ForeignKey(
        ZodiacSign,
        on_delete=models.CASCADE,
    )

class Traits(models.Model):
    Empathy = models.FloatField(default=0)
    Resilience = models.FloatField(default=0)
    Integrity = models.FloatField(default=0)
    Adaptability = models.FloatField(default=0)
    Open_mindedness = models.FloatField(default=0)
    Responsibility = models.FloatField(default=0)
    Confidence = models.FloatField(default=0)
    Perseverance = models.FloatField(default=0)
    Kindness = models.FloatField(default=0)
    Curiosity = models.FloatField(default=0)
    Loyalty = models.FloatField(default=0)
    zodiac_sign = models.ForeignKey(
        ZodiacSign,
        on_delete=models.CASCADE,
    )