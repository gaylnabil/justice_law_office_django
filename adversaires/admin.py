from django.contrib import admin

# Register your models here.

from adversaires.models import Adversaire


@admin.register(Adversaire)
class AdversaireAdmin(admin.ModelAdmin):
    class Meta:
        model = Adversaire
