from parents.parent import Person
from django.db import models
from django.db.models.fields import SlugField
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from justice_law_office.constants import STATUS_JURIDIQUE, CORRESPONDENCE

# Create your models here.

class Adversaire(Person):
    """Model definition for Adversaire."""

    # TODO: Define fields here
    type_adversaire = models.IntegerField(blank=False, null=False, default=1)

    company = models.CharField(
        max_length=255, blank=True, null=True)
    # representant_legal = models.CharField(
    #     max_length=255, blank=True, null=True)

    observation = models.TextField(blank=True, null=True)

    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        """Unicode representation of Adversaire."""
        return f'{self.nom} {self.prenom}'        

    def save(self, *args, **kwargs):
        fullname = f'{self.nom} {self.prenom}'
        self.slug = slugify(fullname)
        super().save(*args, **kwargs)

    class Meta:
        """Meta definition for Adversaire."""
        ordering = ['-id']
        db_table = 'adversaire'
        verbose_name = 'Adversaire'
        verbose_name_plural = 'Adversaires'


class AvocatAdversaire(Person):
    """Model definition for Adversaire."""

    # TODO: Define fields here
    cabinet = models.CharField(
        max_length=255, blank=True, null=True)
    # representant_legal = models.CharField(
    #     max_length=255, blank=True, null=True)

    observation = models.TextField(blank=True, null=True)

    class Meta:
        """Meta definition for Avocat Adversaire."""
        ordering = ['-id']
        db_table = 'avocat_adversaire'
        verbose_name = 'AvocatAdversaire'
        verbose_name_plural = 'AvocatAdversaires'
