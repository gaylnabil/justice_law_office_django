
from django.template.defaultfilters import stringfilter
from django import template


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
