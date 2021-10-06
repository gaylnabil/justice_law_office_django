
from django import forms
from django.forms.widgets import RadioSelect, Textarea
from django.utils.translation import gettext_lazy as _
from clients.models import Client
from justice_law_office.constants import GENDERS, TYPE_PERSON, CORRESPONDENCE
from parents.parent import PersonMixinForm

class ClientForm(PersonMixinForm):
    """Form definition for Client."""

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        
        initials = kwargs.get("initial", {})
        print('Form initial : ', initials)
        self.fields['type_client'].widget.attrs['id'] = 'radio-switch-4'
        self.fields['type_client'].widget.attrs['class'] = 'form-check-input radio-type'
        # self.fields['type_client'].initial = 2
        
        self.fields['nom'].widget.attrs['placeholder'] = _('Nom de client')

        self.fields['prenom'].widget.attrs['placeholder'] = _('Prénom de client')
            
        self.fields['company'].widget.attrs['id'] = 'company-form-2'
        self.fields['company'].widget.attrs['class'] = 'form-control w-full'
        self.fields['company'].widget.attrs['placeholder'] = _('Nom de la société')
        # if initials['type_client'] == 1:
        #     self.fields['company'].widget.attrs['required'] = False
        #     self.fields['company'].widget.attrs['style'] = 'display: none;'
            
            
        # self.fields['representant_legal'].widget.attrs['id'] = 'representant-form-2'
        # self.fields['representant_legal'].widget.attrs['class'] = 'form-control w-full'
        # self.fields['representant_legal'].widget.attrs['placeholder'] = _(
        #     'Nom et Prénom de Representant legal')
            
        self.fields['correspondence'].widget.attrs['id'] = 'radio-switch-4'
        self.fields['correspondence'].widget.attrs['class'] = 'form-check-input'
        
        self.fields['status_juridique'].widget.attrs['id'] = 'status-select'
        self.fields['status_juridique'].widget.attrs['class'] = 'tom-select w-full'
        self.fields['status_juridique'].widget.attrs['data-placeholder'] = _('Selectioner une status juridique')
        

    def clean_company(self):
        return self.cleaned_data['company'].upper()
    class Meta:
        """Meta definition for Clientform."""

        model = Client
        fields = '__all__'
        exclude = ("created_at", "updated_at","slug")
        labels = {
            # TODO: Define fields here
            'type_client': _('type de client'),
            'nom': _('nom'),
            'prenom': _('prénom'),
            'sexe': _('Sexe'),
            'company': _('société'),
            'adresse': _('adresse'),
            'ville': _('Ville'),
            'tel': _('téléphone'),
            'gsm': _('GSM'),
            'email': _('email'),
            'correspondence': _('Correspondence automatique'),
            'status_juridique': _('status juridique'),
            'observation': _('observation')
        }

        widgets = {
            'type_client': RadioSelect(choices=TYPE_PERSON),
            'correspondence': RadioSelect(choices=CORRESPONDENCE),
            'sexe': RadioSelect(choices=GENDERS),
            'adresse': Textarea(attrs=
            {
                'cols': 80, 
                'rows': 5, 
                'placeholder': _('Ajouter votre adresse')
            }),
            
            'observation': Textarea(attrs={
                'cols': 80,
                'rows': 5,
                'placeholder': _("ajouter l'Obeservation")
            }),
        }
        
    
        
