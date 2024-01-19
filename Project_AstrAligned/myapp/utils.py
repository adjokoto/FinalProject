from .models import ZodiacSign, Components


def compare_sign_traits(sign1, sign2):
    sign_one = ZodiacSign.objects.get(id=sign1)
    sign_two = ZodiacSign.objects.get(id=sign2)

    # Get components for both signs
    components1 = Components.objects.filter(zodiac_sign=sign_one)
    components2 = Components.objects.filter(zodiac_sign=sign_two)

    # Find common components for both signs
    common_components = components1.intersection(components2)

    #Calculate % match
    total_components = components1.union(components2)
    component_match = len(common_components)/ len(total_components)

    return {
        'common_components': common_components,
        'component_match': component_match
    }
