from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from justice_law_office.constants import TYPE_AFFAIRES
from parents.parent import PersonMixin, AutoDateTimeField
from clients.models import Client
from adversaires.models import Adversaire, AvocatAdversaire
from django.utils.translation import gettext_lazy as _

# Create your models here.
# model Departement.
class Departement(models.Model):
    """Model definition for Departement."""

    # TODO: Define fields here
    nom_depart = models.CharField(max_length=50, blank=False, null=False)
    
    created_at = models.DateTimeField(
        _("Date de création"), default=timezone.now)

    updated_at = AutoDateTimeField(
        _("Date de modification"), default=timezone.now)

    def __str__(self):
        """Unicode representation of Departement."""
        return self.nom_depart.capitalize()

    class Meta:
        db_table = 'departement'
        managed = True
        """Meta definition for Departement."""
        verbose_name = 'Departement'
        verbose_name_plural = 'Departements'
        ordering = ('-created_at',)
        
        
# model AvocatCharge.
class AvocatCharge(PersonMixin):
    """Model definition for AvocatCharge."""

    # TODO: Define fields here
    observation = models.TextField(blank=True, null=True)

    slug = models.SlugField(blank=True, null=True, max_length=3000)

    def __str__(self):
        """Unicode representation of AvocatCharge."""
        return f'{self.nom} {self.prenom}'

    def save(self, *args, **kwargs):
        fullname = f'{self.nom} {self.prenom}'
        self.slug = slugify(fullname)
        super().save(*args, **kwargs)

    class Meta:
        """Meta definition for AvocatCharge."""
        db_table = 'avocat_charge'
        managed = True
        verbose_name = 'AvocatCharge'
        verbose_name_plural = 'AvocatCharges'
        ordering = ('-created_at',)

# model Affaire.
class Affaire(models.Model):
    
    reference = models.CharField(max_length=50, blank=True, null=True)
    date_dossier = models.DateField(
        default=timezone.now, blank=False, null=False)
    date_presc = models.DateField(default=timezone.now, blank=True, null=True)
    
    type_affaire = models.CharField(max_length=50, blank=False, null=False, choices=TYPE_AFFAIRES, default='civil')
    
    complementaire = models.CharField(max_length=50, blank=False, null=False, choices=TYPE_AFFAIRES, default='standard')
    
    objet = models.CharField(blank=True, null=True, max_length=50)
    
    client_id = models.ForeignKey(Client, blank=True, null=True, on_delete=models.PROTECT)
    adversaire_id = models.ForeignKey(Adversaire, blank=True, null=True, on_delete=models.SET_NULL)
    avocat_adv_id = models.ForeignKey(AvocatAdversaire, blank=True, null=True, on_delete=models.SET_NULL)
    
    department_id = models.ForeignKey(Departement, blank=True, null=True, on_delete=models.PROTECT)
    charge_id = models.ForeignKey(AvocatCharge, blank=True, null=True, on_delete=models.PROTECT)
    
    created_at = models.DateTimeField(
        _("Date de création"), default=timezone.now)

    updated_at = AutoDateTimeField(
        _("Date de modification"), default=timezone.now)
    
    def __str__(self):
        return self.reference
    class Meta:
        db_table = 'affaire'
        managed = True
        verbose_name = 'Affaire'
        verbose_name_plural = 'Affaires'
        ordering = ('-created_at',)
        
        

