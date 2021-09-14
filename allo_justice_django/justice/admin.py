from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext as _
from accounts.models import Attorney, City, Schedule
from clients.models import Client
from justice.models import Question

# Register your models here.
# admin.site.unregister(Attorney)

# admin.site.register(Attorney)

admin.site.register(City)
admin.site.register(Schedule)
admin.site.register(Client)
admin.site.register(Question)
