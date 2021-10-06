from django.db import models
from django.template.defaultfilters import slugify

from parents.parent import PersonMixin

# Create your models here.
class Affaire(models.Model):
    
    def __str__(self):
        pass

    class Meta:
        db_table = 'affaire'
        managed = True
        verbose_name = 'Affaire'
        verbose_name_plural = 'Affaires'
        
        
# Create your models here.
class AvocatCharge(PersonMixin):
    """Model definition for AvocatCharge."""

    # TODO: Define fields here
    observation = models.TextField(blank=True, null=True)

    slug = models.SlugField(blank=True, null=True)

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
        