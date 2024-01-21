from .models import *
from django.db import models
from django.shortcuts import render


def compare_components(components1, components2):
    """
    Compares the traits of two Traits instances.
    Returns a list of attributes with a score difference of <= 1.
    """
    common_components = []
    if not (isinstance(components1, Components) and isinstance(components2, Components)):
        raise ValueError("Both arguments must be instances of Components")

    for field in Components._meta.get_fields():
        # Ensure the field is a FloatField and not a ForeignKey
        exclude_list = ["zodiac_sign","id","ruling_planet_one","ruling_planet_two"]
        if field.name not in exclude_list:
        # Get the value of the field for both instances
            value1 = getattr(components1, field.name, 0)
            value2 = getattr(components2, field.name, 0)

            # Check if the difference is less than or equal to 1
            if (value1 == value2) and (not (value1 == "")):
                common_components.append(field.name)
    if(components1.ruling_planet_one == components2.ruling_planet_one or components1.ruling_planet_one == components2.ruling_planet_two
    or components1.ruling_planet_two == components2.ruling_planet_two):
        common_components.append("ruling planet")
    print("final common components")
    print(common_components)
    return common_components

def compare_traits(traits1, traits2):
    """
    Compares the traits of two Traits instances.
    Returns a list of attributes with a score difference of <= 1.
    """
    common_traits = []
    if not isinstance(traits1, Traits) or not isinstance(traits2, Traits):
        raise ValueError("Both arguments must be instances of Traits")

    for field in Traits._meta.get_fields():
        if isinstance(field, models.FloatField):
            value1 = getattr(traits1, field.name, 0)
            value2 = getattr(traits2, field.name, 0)

            if abs(value1 - value2) <= 2:
                common_traits.append(field.name)

    return common_traits


def compare_signs(sign_one, sign_two):

    components1 = Components.objects.filter(zodiac_sign__sign=sign_one.lower())[0]
    components2 = Components.objects.filter(zodiac_sign__sign=sign_two.lower())[0]

    traits1 = Traits.objects.filter(zodiac_sign__sign=sign_one.lower())[0]
    traits2 = Traits.objects.filter(zodiac_sign__sign=sign_two.lower())[0]

    common_components = compare_components(components1,components2)
    common_traits = compare_traits(traits1, traits2)

    total_components = Components.COMPONENT_FIELDS_COUNT
    total_traits = Traits.TRAIT_FIELDS_COUNT

    component_match = (len(common_components) / total_components) * 100
    trait_match = (len(common_traits) / total_traits) * 100

    return {
        'common_components': common_components,
        'component_match': component_match,
        'common_traits': common_traits,
        'trait_match': trait_match
    }