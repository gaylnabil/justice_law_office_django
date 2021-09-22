from django.contrib import admin

from clients.models import Client

# Register your models here.


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    
    readonly_fields = ("created_at", "updated_at",)
    
    class Meta:
        model = Client


    
