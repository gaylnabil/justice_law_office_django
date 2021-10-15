from django.contrib import admin

# Register your models here.
from adversaires.models import Adversaire, AvocatAdversaire


@admin.register(Adversaire)
class AdversaireAdmin(admin.ModelAdmin):
    
    readonly_fields = ("created_at", "updated_at",)
    list_display = [field.name for field in Adversaire._meta.fields]
    class Meta:
        model = Adversaire
        
        
@admin.register(AvocatAdversaire)
class AvocatAdversaireAdmin(admin.ModelAdmin):

    readonly_fields = ("created_at", "updated_at",)
    list_display = [field.name for field in AvocatAdversaire._meta.fields]

    class Meta:
        model = AvocatAdversaire
