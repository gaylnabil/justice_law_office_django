from django import forms
from django.forms.widgets import RadioSelect, Textarea
from django.utils.translation import gettext_lazy as _
from affaires.models import AvocatCharge
from justice_law_office.constants import GENDERS, TYPE_PERSON
from parents.parent import PersonMixinForm

class AvocatChargeForm(PersonMixinForm):
    """Form definition for AvocatCharge."""

    def __init__(self, *args, **kwargs):
        super(AvocatChargeForm, self).__init__(*args, **kwargs)

        # self.fields['type_adversaire'].widget.attrs['id'] = 'radio-switch-4'
        # self.fields['type_adversaire'].widget.attrs['class'] = 'form-check-input radio-type'
        # self.fields['type_adversaire'].initial = 2

        self.fields['nom'].widget.attrs['placeholder'] = _("Nom d'avocat")

        self.fields['prenom'].widget.attrs['placeholder'] = _(
            "Prénom d'avocat")

        self.fields['sexe'].initial = 'M'

    class Meta:
        """Meta definition for AvocatChargeForm."""

        model = AvocatCharge
        fields = '__all__'
        exclude = ("created_at", "updated_at", "slug")
        labels = {
            # TODO: Define fields here
            'nom': _('nom'),
            'prenom': _('prénom'),
            'sexe': _('Sexe'),
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
                'placeholder': _("Ajouter l'Obeservation")
            }),
        }
