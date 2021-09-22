from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from justice_law_office.constants import VILLES, STATUS_JURIDIQUE, GENDERS

# Create your models here.


class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()

class Client(models.Model):
    """Model definition for Client."""
    
    # TODO: Define fields here
    type_client = models.IntegerField(blank=False, null=False, default=1)
    nom = models.CharField(max_length = 100, blank = True, null = True)
    prenom = models.CharField(max_length=100, blank=True, null=True)
    
    sexe = models.CharField(max_length=1, blank=True,
                            null=True, default='M')
    
    company = models.CharField(
        max_length = 255, blank = True, null = True)
    # representant_legal = models.CharField(
    #     max_length=255, blank=True, null=True)

    adresse = models.TextField(blank=True, null=True)
    # siege_social = models.TextField(blank = False, null = False)
    ville = models.IntegerField(blank=False, null=False, choices=VILLES, default=23)
    tel = models.CharField(max_length = 50, blank = True, null = True)
    gsm = models.CharField(max_length = 50, blank = True, null = True)
    email = models.CharField(max_length = 50, blank = True, null = True)
    
    status_juridique = models.IntegerField(
        blank=True, null=True, choices=STATUS_JURIDIQUE)

    observation = models.TextField(blank = True, null = True)
    
    created_at = models.DateTimeField(
        _("Date de création"), default=timezone.now)
        
    updated_at = AutoDateTimeField(
        _("Date de modification"), default=timezone.now)

    class Meta:
        """Meta definition for Client."""
        ordering = ['-id']
        db_table = 'client'
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        """Unicode representation of Client."""
        return f'{self.nom} {self.prenom}' 


