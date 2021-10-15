from django.contrib import admin

from affaires.models import AvocatCharge, Departement

# Register your models here.


@admin.register(AvocatCharge)
class AdversaireAdmin(admin.ModelAdmin):

    readonly_fields = ("created_at", "updated_at",)
    list_display = [field.name for field in AvocatCharge._meta.fields]

    class Meta:
        model = AvocatCharge
        
        
@admin.register(Departement)
class DepartementAdmin(admin.ModelAdmin):

    readonly_fields = ("created_at", "updated_at",)
    list_display = [field.name for field in Departement._meta.fields]

    class Meta:
        model = Departement
