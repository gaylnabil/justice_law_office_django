from django.db import models
from justice_law_office.constants import GENDERS, VILLES
from django.utils import timezone
from django.template.defaultfilters import slugify
from django import forms
from django.forms.widgets import RadioSelect, Textarea
from django.utils.translation import gettext_lazy as _
from justice_law_office.constants import GENDERS, TYPE_PERSON

class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()
        
        
class Person(models.Model):
    
    nom = models.CharField(max_length= 100, blank = True, null = True)
    prenom = models.CharField(max_length=100, blank=True, null=True)
    
    sexe = models.CharField(max_length=1, blank=False,
                            null=False, choices=GENDERS, default='M')
                            
    adresse = models.TextField(blank=True, null=True)
    # siege_social = models.TextField(blank = False, null = False)
    ville = models.CharField(max_length=30, blank=False, null=False,
                             choices=VILLES, default='Casablanca')
    tel = models.CharField(max_length=50, blank=True, null=True)
    gsm = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    
    slug = models.SlugField(blank=True, null=True)

    
    created_at = models.DateTimeField(
        _("Date de création"), default=timezone.now)

    updated_at = AutoDateTimeField(
        _("Date de modification"), default=timezone.now)

    def __str__(self):
        """Unicode representation of Person."""
        return f'{self.nom} {self.prenom}'
 
    def save(self, *args, **kwargs):
        fullname = f'{self.nom} {self.prenom}'
        self.slug = slugify(fullname)
        super().save(*args, **kwargs)
        
    class Meta:
        abstract = True
        
        
# Form definition for Person ***************************************

class PersonForm(forms.ModelForm):
    """Form definition for Adversaire."""

    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)

        initials = kwargs.get("initial", {})

        self.fields['nom'].widget.attrs['id'] = 'nom-form-1'
        self.fields['nom'].widget.attrs['class'] = 'form-control w-full'
        self.fields['nom'].widget.attrs['data-adversaire'] = 'moral'

        self.fields['prenom'].widget.attrs['id'] = 'prenom-form-2'
        self.fields['prenom'].widget.attrs['class'] = 'form-control w-full'
        self.fields['prenom'].widget.attrs['data-adversaire'] = 'physique'

        self.fields['sexe'].widget.attrs['id'] = 'radio-switch-4'
        self.fields['sexe'].widget.attrs['class'] = 'form-check-input'
        self.fields['sexe'].initial = 'M'


        self.fields['adresse'].widget.attrs['id'] = 'adresse-form'
        self.fields['adresse'].widget.attrs['class'] = 'form-control w-full'

        self.fields['ville'].widget.attrs['id'] = 'cities-select'
        self.fields['ville'].widget.attrs['class'] = 'tom-select w-full'
        self.fields['ville'].widget.attrs['data-placeholder'] = _('Selectioner une ville')
        # self.fields['ville'].initial = 23

        self.fields['gsm'].widget.attrs['id'] = 'gsm-id'
        self.fields['gsm'].widget.attrs['class'] = 'form-control'
        self.fields['gsm'].widget.attrs['type'] = 'tel'
        self.fields['gsm'].widget.attrs['placeholder'] = _('GSM')
        self.fields['gsm'].widget.attrs['aria-describedby'] = 'input-group-3'

        self.fields['tel'].widget.attrs['id'] = 'tel-id'
        self.fields['tel'].widget.attrs['class'] = 'form-control'
        self.fields['tel'].widget.attrs['type'] = 'tel'
        self.fields['tel'].widget.attrs['placeholder'] = _('teléphone')
        self.fields['tel'].widget.attrs['aria-describedby'] = 'input-group-3'

        self.fields['email'].widget.attrs['id'] = 'email-id'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['type'] = 'email'
        self.fields['email'].widget.attrs['placeholder'] = _('email')
        self.fields['email'].widget.attrs['aria-describedby'] = 'input-group-3'

    def clean_nom(self):
        return self.cleaned_data['nom'].upper()

    def clean_prenom(self):
        return self.cleaned_data['prenom'].capitalize()

    class Meta:
        """Meta definition for Personform."""

        model = Person
        fields = '__all__'
        # exclude = ("created_at", "updated_at", "slug")
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
        }

        widgets = {
            'sexe': RadioSelect(choices=GENDERS),
            'adresse': Textarea(attrs={
                'cols': 80,
                'rows': 5,
                'placeholder': _('Ajouter votre adresse')
            }),

        }
