from parents.parent import PersonMixin
from django.db import models
from django.db.models.fields import SlugField
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from justice_law_office.constants import STATUS_JURIDIQUE, CORRESPONDENCE

# Create your models here.


class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()

class Client(PersonMixin):
    """Model definition for Client."""
    
    # TODO: Define fields here
    type_client = models.IntegerField(blank=False, null=False, default=1)
    
    company = models.CharField(
        max_length = 255, blank = True, null = True)
    # representant_legal = models.CharField(
    #     max_length=255, blank=True, null=True)
    correspondence = models.CharField(max_length=5, blank=False, null=False,
                                         choices=CORRESPONDENCE, default='apres')

    status_juridique = models.IntegerField(
        blank=True, null=True, choices=STATUS_JURIDIQUE)

    observation = models.TextField(blank = True, null = True)
    
    slug = models.SlugField(blank=True, null=True)
    
    created_at = models.DateTimeField(
        _("Date de création"), default=timezone.now)
        
    updated_at = AutoDateTimeField(
        _("Date de modification"), default=timezone.now)
    
    def __str__(self):
        """Unicode representation of Client."""
        return f'{self.nom} {self.prenom}' 
    
    def save(self, *args, **kwargs):
        fullname = f'{self.nom} {self.prenom}'
        self.slug = slugify(fullname)
        super().save(*args, **kwargs)
        
    class Meta:
        """Meta definition for Client."""
        ordering = ['-id']
        db_table = 'client'
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'




