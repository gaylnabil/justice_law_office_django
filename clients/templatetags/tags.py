
from django.template.defaultfilters import stringfilter
from django import template
from justice_law_office.constants import VILLES

register = template.Library()


@register.filter(name='trim')
@stringfilter
def trim(value):
    return value.strip()


@register.filter(name='divide')
def divide(value, arg):
    try:
        return int(value) / int(arg)
    except (ValueError, ZeroDivisionError):
        return None
        

@register.filter(name='multiply')
def multiply(value, arg):
    return int(value) * int(arg)
    

@register.filter(name='city_name')
def city_name(value):
    
    list = dict(VILLES)
    
    return list[value]
