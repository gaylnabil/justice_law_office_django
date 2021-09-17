
from django import forms
from django.forms.widgets import RadioSelect, Textarea
from django.utils.translation import gettext_lazy as _
from clients.models import Client
from justice_law_office.constants import TYPE_CLIENT, VILLES



class ClientForm(forms.ModelForm):
    """Form definition for Client."""

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)

        self.fields['type_client'].widget.attrs['id'] = 'radio-switch-4'
        self.fields['type_client'].widget.attrs['class'] = 'form-check-input'
        self.fields['type_client'].initial = 1
        
        self.fields['nom'].widget.attrs['id'] = 'crud-form-1'
        self.fields['nom'].widget.attrs['class'] = 'form-control w-full'
        self.fields['nom'].widget.attrs['placeholder'] = _('Nom de client')

        self.fields['prenom'].widget.attrs['id'] = 'crud-form-2'
        self.fields['prenom'].widget.attrs['class'] = 'form-control w-full'
        self.fields['prenom'].widget.attrs['placeholder'] = _(
            'Prénom de client')
            
        self.fields['ville'].widget.attrs['id'] = 'cities-select'
        self.fields['ville'].widget.attrs['class'] = 'tom-select w-full'
        self.fields['ville'].widget.attrs['data-placeholder'] = _(
            'Selectioner une ville')
        self.fields['ville'].initial = 23
        
        self.fields['tel'].widget.attrs['id'] = 'tel-id'
        self.fields['tel'].widget.attrs['class'] = 'form-control'
        self.fields['tel'].widget.attrs['type'] = 'tel'
        self.fields['tel'].widget.attrs['placeholder'] = _('teléphone')
        self.fields['tel'].widget.attrs['aria-describedby'] = 'input-group-3'
       
        
        self.fields['gsm'].widget.attrs['id'] = 'gsm-id'
        self.fields['gsm'].widget.attrs['class'] = 'form-control'
        self.fields['gsm'].widget.attrs['type'] = 'tel'
        self.fields['gsm'].widget.attrs['placeholder'] = _('GSM')
        self.fields['gsm'].widget.attrs['aria-describedby'] = 'input-group-3'
        
        self.fields['email'].widget.attrs['id'] = 'email-id'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['type'] = 'email'
        self.fields['email'].widget.attrs['placeholder'] = _('email')
        self.fields['email'].widget.attrs['aria-describedby'] = 'input-group-3'
        
        self.fields['status_juridique'].widget.attrs['id'] = 'status-select'
        self.fields['status_juridique'].widget.attrs['class'] = 'tom-select w-full'
        self.fields['status_juridique'].widget.attrs['data-placeholder'] = _(
            'Selectioner une status juridique')
            
    class Meta:
        """Meta definition for Clientform."""

        model = Client
        fields = '__all__'
        labels = {
            # TODO: Define fields here
            'type_client': _('type de client'),
            'nom': _('nom'),
            'prenom': _('prénom'),
            'personne_moral': _('société'),
            'presentant_legal': _('représental légal'),
            'adresse': _('adresse'),
            'ville': _('ville'),
            'tel': _('téléphone'),
            'gsm': _('GSM'),
            'email': _('email'),
            'status_juridique': _('status juridique'),
            'observation': _('observation')
        }

        widgets = {
            'type_client': RadioSelect(choices=TYPE_CLIENT),
            'adresse': Textarea(attrs=
            {
                'cols': 80, 
                'rows': 5, 
                'placeholder': _('ajouter une adresse')
            }),
            
            'observation': Textarea(attrs={
                'cols': 80,
                'rows': 5,
                'placeholder': _("ajouter l'Obeservation")
            }),
        }
        
    
        
