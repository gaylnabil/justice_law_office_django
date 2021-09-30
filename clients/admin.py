from django.contrib import admin

# Register your models here.

from clients.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):

    readonly_fields = ("created_at", "updated_at",)

    class Meta:
        model = Client
