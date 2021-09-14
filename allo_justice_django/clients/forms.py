
from accounts.models import Attorney
from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from clients.models import Client
from django.utils.text import capfirst
from crispy_forms.helper import FormHelper
from django.utils.translation import gettext as _
from accounts.widgets import AdminImageWidget
from accounts.utils import Mode, resize_image


class ClientCreationForm(UserCreationForm):

    class Meta:
        model = Client
        fields = ('first_name', 'last_name', 'username',
                  'email', 'password1', 'password2', 'is_active')
        # exclude = ['is_superuser', 'is_staff', 'is_active', 'date_joined']
        labels = {
            # 'first_name': _('Prénom'),
            # 'last_name': _('Nom'),
            'password1': _('Mot de passe'),
            'password2': _('Confirmez'),
        }

    def __init__(self, *args, **kwargs):
        super(ClientCreationForm, self).__init__(*args, **kwargs)
        pass


class ClientUpdateForm(UserChangeForm):

    class Meta:
        model = Client

        fields = (
            'first_name',
            'last_name',
            'sex',
            'address',
            'building',
            'neighborhood',
            'indication',
            'city',
            'tel',
            'gsm',
            'zip_code',

        )
        # exclude = ['is_superuser', 'is_staff', 'is_active', 'date_joined','password1', 'password2' ]

        labels = {
            'first_name': _('Prénom'),
            'last_name': _('Nom'),
            'sex': _('Sexe'),
            'address': _('Numéro et rue du cabinet'),
            'building': _('Appartement / Immeuble'),
            'neighborhood': _('Quartier'),
            'indication': _('Indication'),
            'city': _('Ville'),
            'zip_code': _('Code Postale'),
            'tel': _('Téléphone'),
            'gsm': _('GSM'),

            # 'profile_image': _('Upload Image'),
        }


class ClientAuthenticationForm(AuthenticationForm):

    class Meta:
        model = Client
        fields = ('username', 'password', 'type')

    def __init__(self, *args, **kwargs):
        super(ClientAuthenticationForm, self).__init__(*args, **kwargs)
        pass
