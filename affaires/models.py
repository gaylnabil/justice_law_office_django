from django.db import models

# Create your models here.
class Affaire(models.Model):
    
    def __str__(self):
        pass

    class Meta:
        db_table = 'affaire'
        managed = True
        verbose_name = 'Affaire'
        verbose_name_plural = 'Affaires'
