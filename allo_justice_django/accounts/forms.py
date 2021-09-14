
from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from accounts.models import Attorney, Schedule
from django.utils.text import capfirst
from crispy_forms.helper import FormHelper
from django.utils.translation import gettext as _
from accounts.widgets import AdminImageWidget
from accounts.utils import Mode, resize_image


class AttorneyCreationForm(UserCreationForm):

    # email = forms.EmailField(label=_('Adresse électronique'), widget=forms.TextInput(
    #     attrs={'type': 'email',
    #            'placeholder': _('abc@xyz.com')}), required=True)
    # first_name = forms.CharField(label=_('Prénom'), required=True)
    # last_name = forms.CharField(label=_('Nom'), required=True)

    def __init__(self, *args, **kwargs):
        super(AttorneyCreationForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['required'] = True
        self.fields['last_name'].widget.attrs['required'] = True

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if not first_name:
            raise ValidationError(_('Le prénom est obligatoire'))

        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')

        if not last_name:
            raise ValidationError(_('le nom est obligatoire'))

        return last_name

    class Meta:
        model = Attorney
        fields = ('first_name', 'last_name', 'username',
                  'email', 'password1', 'password2', 'is_active')
        #exclude = ['is_superuser', 'is_staff', 'date_joined']

        # exclude = ['is_superuser', 'is_staff', 'is_active', 'date_joined']
        # labels = {
        #     'username': _("Nom d'utilisateur"),
        #     'first_name': _('Prénom'),
        #     'last_name': _('Nom'),
        #     'password1': _('Mot de passe'),
        #     'password2': _('Confirmez'),
        # }


class AttorneyUpdateForm(UserChangeForm):

    # profile_image = forms.EmailField(label=_('Choisir photo de profile'), widget=forms.TextInput(
    # attrs={'type': 'file'}), required=False)

    profile_image = forms.ImageField(
        label=_('Choisir photo de profile'), widget=forms.FileInput(), required=False)

    def __init__(self, *args, **kwargs):
        super(AttorneyUpdateForm, self).__init__(*args, **kwargs)
        self.fields['profile_image'].widget.attrs['class'] = 'gayl_nabil'

    class Meta:
        model = Attorney

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
            'education',
            'presentation',
            'experience',
            'skill',
            'web',
            'facebook',
            'instagram',
            'youtube',
            'web',
            'video',
            'rib',
            'profile_image',
        )
        # exclude = ['is_superuser', 'is_staff', 'is_active', 'date_joined','password1', 'password2' ]

        labels = {
            # 'first_name': _('Prénom'),
            # 'last_name': _('Nom'),
            'sex': _('Sexe'),
            'address': _('Numéro et rue du cabinet'),
            'building': _('Appartement / Immeuble'),
            'neighborhood': _('Quartier'),
            'indication': _('Indication'),
            'city': _('Ville'),
            'zip_code': _('Code Postale'),
            'tel': _('Téléphone'),
            'gsm': _('GSM'),
            'presentation': _('Présentation'),
            'education': _('Formations'),
            'experience': _('Expériences'),
            'skill': _('Compétence'),
            'web': _('Site Web'),
            'facebook': _('Facebook'),
            'instagram': _('Instagram'),
            'youtube': _('YouTube'),
            'video': _('Ma Vidéo'),
            'rib': _('RIB'),
            # 'profile_image': _('Upload Image'),
        }

        # def clean_profile_image(self):
        #     image = self.cleaned_data['profile_image']
        #     if image is not None:
        #         print(image.name)
        #         image = resize_image(image.name, (471, 470), Mode.FIT)
        #     # Always return a value to use as the new cleaned data, even if
        #     # this method didn't change it.
        #     return image


class AttorneyAuthenticationForm(AuthenticationForm):
    class Meta:
        model = Attorney
        fields = ('username', 'password', 'type')

    # def __init__(self, *args, **kwargs):
    #     super(AttorneyAuthenticationForm, self).__init__(*args, **kwargs)


class ScheduleAttorneyForm(forms.ModelForm):

    class Meta:
        model = Schedule
        fields = '__all__'
        # exclude = ['attorney']
        labels = {
            'day_name': _('Jour'),
            'time_from': _('De'),
            'time_to': _('à'),
        }

    def __init__(self, *args, **kwargs):
        super(ScheduleAttorneyForm, self).__init__(*args, **kwargs)

        self.fields['day_name'].widget.attrs['readonly'] = 'readonly'
        self.fields['day_name'].widget.attrs['class'] = 'day_name'
        self.fields['day_name'].widget.attrs['style'] = 'border-color: transparent;'
        self.fields['day_name'].widget.attrs['style'] = 'background-color: transparent;'
        # Textarea(attrs={'style': 'border-color: orange;'}),
