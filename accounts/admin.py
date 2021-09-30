from django.contrib import admin

from accounts.models import Avocat

# Register your models here.


@admin.register(Avocat)
class accountAdmin(admin.ModelAdmin):
    
    class Meta:
        model = Avocat


    
