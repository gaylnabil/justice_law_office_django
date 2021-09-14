
from django.forms import forms
from django.utils.translation import gettext_lazy as _
from clients.models import Client


class ClientForm(forms.ModelForm):
    """Form definition for Client."""

    class Meta:
        """Meta definition for Clientform."""

        model = Client
        fields = '__all__'
        label={
            # TODO: Define fields here
            'type_client' : _('type de client'),
            'nom': _('nom'),
            'prenom' :_('prénom'),
            'personne_moral': _('société'),

            'presentant_legal' :_('représental légal'),
            'adresse' : _('adresse'),
            'ville': _('ville'),
            'tel' : _('téléphone'),
            'gsm' : _('gsm'),
            'email' : _('email'),
            'status_juridique' : _('status juridique'),
            'observation': _('observation')
        }
        
