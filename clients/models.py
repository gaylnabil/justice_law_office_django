from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from justice_law_office.constants import VILLES
# Create your models here.

class Client(models.Model):
    """Model definition for Client."""

    # TODO: Define fields here
    type_client = models.CharField(max_length = 50, blank = False, null = False)
    nom = models.CharField(max_length = 100, blank = True, null = True)
    prenom = models.CharField(max_length=100, blank=True, null=True)
    personne_moral = models.CharField(
        max_length = 255, blank = True, null = True)

    presentant_legal = models.CharField(
        max_length = 255, blank = False, null = False)

    adresse = models.TextField(blank = False, null = False)
    # siege_social = models.TextField(blank = False, null = False)
    ville = models.CharField(max_length=50, blank=True,
                             null=True, choices=VILLES)
    tel = models.CharField(max_length = 50, blank = True, null = True)
    gsm = models.CharField(max_length = 50, blank = True, null = True)
    email = models.CharField(max_length = 50, blank = True, null = True)
    
    status_juridique = models.CharField(
        max_length = 50, blank = True, null = True)

    observation = models.TextField(blank = True, null = True)
    #user_id = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Client."""
        db_table = 'client'
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        """Unicode representation of Client."""
        return f'{self.nom} {self.prenom}' 
