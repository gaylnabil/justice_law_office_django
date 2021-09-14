from django.contrib import admin
from django.contrib.auth.models import User
from django.utils.html import mark_safe
from accounts.models import Attorney
from django.contrib.auth.admin import UserAdmin
from accounts.widgets import AdminImageWidget
from django.db import models
from django import forms
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext as _
# Register your models here.


class AttorneyAdminCreationForm(UserCreationForm):

    class Meta:
        model = Attorney
        fields = ('username', 'password1', 'password2')
        #exclude = ['is_superuser', 'is_staff', 'date_joined']

        # exclude = ['is_superuser', 'is_staff', 'is_active', 'date_joined']
        # labels = {
        #     'first_name': _('Prénom'),
        #     'last_name': _('Nom'),
        #     'password1': _('Mot de passe'),
        #     'password2': _('Confirmez'),
        # }


@admin.register(Attorney)
class AttorneyAdmin(UserAdmin):
    model = Attorney
    add_form = AttorneyAdminCreationForm

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Other Information',
            {
                'fields': ('address', 'building', 'neighborhood', 'indication', 'zip_code', 'tel', 'gsm', 'web', 'profile_image')
            }
        )
    )
