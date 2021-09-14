
import base64
import hashlib
from datetime import datetime
from allo_justice_django.settings import ENCRYPT_KEY, LANGUAGE_CODE
from cryptography.fernet import Fernet
from django.template.defaultfilters import stringfilter
from django import template


class SetVarNode(template.Node):

    def __init__(self, var_name, var_value):
        self.var_name = var_name
        self.var_value = var_value

    def render(self, context):
        try:
            value = template.Variable(self.var_value).resolve(context)
        except template.VariableDoesNotExist:
            value = ""
        context[self.var_name] = value

        return u''


register = template.Library()


@register.tag(name='set')
def set_var(parser, token):
    """
    {% set some_var = '123' %}
    """
    parts = token.split_contents()
    if len(parts) < 4:
        raise template.TemplateSyntaxError(
            "'set' tag must be of the form: {% set <var_name> = <var_value> %}")

    return SetVarNode(parts[1], parts[3])


@register.filter(name='encrypt')
def encrypt(value):
    # key = Fernet.generate_key()
    # print(f"My key ===> {key}")
    frt = Fernet(ENCRYPT_KEY)
    value = value.encode()
    encrypted = frt.encrypt(value)
    return encrypted.decode()


@register.filter(name='decrypt')
def decrypt(value):
    frt = Fernet(ENCRYPT_KEY)
    value = value.encode()
    decrypted = frt.decrypt(value)
    return decrypted.decode()


@register.filter(name='trim')
@stringfilter
def trim(value):
    return value.strip()


@register.filter(name='class_name')
def class_name(object):
    return object._meta.verbose_name

# @register.filter(name='decrement')
# @stringfilter
# def increment(value):
#     return value - 1

# @register.filter(name='increment')
# @stringfilter
# def increment(value):
#     return value + 1


# import base64
# import os
# from cryptography.fernet import Fernet
# from cryptography.hazmat.primitives import hashes
# from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
# import onetimepad

# def encryptTxt(txt):
#    txt =   'c0f*'+ txt +'J$n2A?'
#    return onetimepad.encrypt(txt, str(ENCRYPT_KEY))

# def decryptTxt(txt):
#    return onetimepad.decrypt(txt, str(ENCRYPT_KEY))
