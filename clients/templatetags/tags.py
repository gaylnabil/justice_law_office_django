
from django.template.defaultfilters import stringfilter
from django import template
from justice_law_office.constants import PAGES, VILLES

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
def city_name(key):
    
    dictionary = dict(VILLES)
    if key in dictionary:
        return dictionary[key]
    return ''
    
    
@register.simple_tag
def string_to_list(value, separator):
    if isinstance(value, str):
        return value.split(separator)
    return []   

@register.filter(name='page_name') 
def page_name(key):
    if key in PAGES:
        return PAGES[key]
    return None
