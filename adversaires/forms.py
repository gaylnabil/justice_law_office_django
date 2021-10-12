
from django import forms
from django.forms.widgets import RadioSelect, Textarea
from django.utils.translation import gettext_lazy as _
from adversaires.models import Adversaire, AvocatAdversaire
from justice_law_office.constants import GENDERS, TYPE_PERSON
from parents.parent import PersonMixinForm


class AdversaireForm(PersonMixinForm):
    """Form definition for Adversaire."""

    def __init__(self, *args, **kwargs):
        super(AdversaireForm, self).__init__(*args, **kwargs)

        initials = kwargs.get("initial", {})
        print('Form initial : ', initials)
        self.fields['type_adversaire'].widget.attrs['id'] = 'radio-switch-4'
        self.fields['type_adversaire'].widget.attrs['class'] = 'form-check-input radio-type'
        # self.fields['type_adversaire'].initial = 2
        
        self.fields['nom'].widget.attrs['placeholder'] = _("Nom d'adversaire")

        self.fields['prenom'].widget.attrs['placeholder'] = _('Prénom de adversaire')

        # if initials['type_adversaire'] == 1:
        #     self.fields['company'].widget.attrs['required'] = False
        #     self.fields['company'].widget.attrs['style'] = 'display: none;'

        # self.fields['representant_legal'].widget.attrs['id'] = 'representant-form-2'
        # self.fields['representant_legal'].widget.attrs['class'] = 'form-control w-full'
        # self.fields['representant_legal'].widget.attrs['placeholder'] = _(
        #     'Nom et Prénom de Representant legal')

    def clean_company(self):
        value = self.cleaned_data['company']
        if value:
            return value.upper()
    class Meta:
        """Meta definition for Adversaireform."""

        model = Adversaire
        fields = '__all__'
        exclude = ("created_at", "updated_at", "slug")
        labels = {
            # TODO: Define fields here
            'type_adversaire': _("type d'adversaire"),
            'nom': _('nom'),
            'prenom': _('prénom'),
            'sexe': _('Sexe'),
            'company': _('société'),
            'adresse': _('adresse'),
            'ville': _('Ville'),
            'tel': _('téléphone'),
            'gsm': _('GSM'),
            'email': _('email'),
            # 'status_juridique': _('status juridique'),
            'observation': _('observation')
        }

        widgets = {
            'type_adversaire': RadioSelect(choices=TYPE_PERSON),
            'sexe': RadioSelect(choices=GENDERS),

            'observation': Textarea(attrs={
                'cols': 80,
                'rows': 5,
                'placeholder': _("ajouter l'Obeservation")
            }),
        }
        
        
class AvocatAdversaireForm(PersonMixinForm):
    """Form definition for AvocatAdversaireForm."""

    def __init__(self, *args, **kwargs):
        super(AvocatAdversaireForm, self).__init__(*args, **kwargs)

        # self.fields['type_adversaire'].widget.attrs['id'] = 'radio-switch-4'
        # self.fields['type_adversaire'].widget.attrs['class'] = 'form-check-input radio-type'
        # self.fields['type_adversaire'].initial = 2

        self.fields['nom'].widget.attrs['placeholder'] = _("Nom d'avocat")

        self.fields['prenom'].widget.attrs['placeholder'] = _("Prénom d'avocat")

        self.fields['sexe'].initial = 'M'

        self.fields['cabinet'].widget.attrs['placeholder'] = _(
            "Nom de cabinet")

    def clean_cabinet(self):
        value = self.cleaned_data['cabinet']
        if value:
            return value.upper()
        return value
        
        
    class Meta:
        """Meta definition for AvocatAdversaireForm."""

        model = AvocatAdversaire
        fields = '__all__'
        exclude = ("created_at", "updated_at", "slug", "type_adversaire")
        labels = {
            # TODO: Define fields here
            'nom': _('nom'),
            'prenom': _('prénom'),
            'sexe': _('Sexe'),
            'cabinet': _('Cabinet'),
            'adresse': _('adresse'),
            'ville': _('Ville'),
            'tel': _('téléphone'),
            'gsm': _('GSM'),
            'email': _('email'),
            'observation': _('observation')
        }

        widgets = {
            'sexe': RadioSelect(choices=GENDERS),
            'adresse': Textarea(attrs={
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
