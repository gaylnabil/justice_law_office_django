from django.db import models

# Create your models here.


class Client(object):
    def __init__(self, *args):
        super(Client, self).__init__(*args))


class Client(models.Model):
    """Model definition for Client."""


    # TODO: Define fields here
    type_client=models.CharField(max_length = 50, blank = True, null = True)
    nom=models.CharField(max_length = 100, blank = True, null = True)
    prenom=models.CharField(max_length = 100, blank = False, null = False)
    personne_moral=models.CharField(
        max_length = 255, blank = True, null = True)

    presentant_legal=models.CharField(
        max_length = 255, blank = False, null = False)

    adresse=models.TextField(blank = False, null = False)
    # siege_social = models.TextField(blank = False, null = False)
    ville=models.CharField(max_length = 50, blank = True, null = True)
    tel=models.CharField(max_length = 50, blank = True, null = True)
    gsm=models.CharField(max_length = 50, blank = True, null = True)
    email=models.CharField(max_length = 50, blank = True, null = True)

    status_juridique=models.CharField(
        max_length = 50, blank = True, null = True)

    observation=models.TextField(blank = True, null = True)


    class Meta:
        """Meta definition for Client."""
        db_table='client'
        verbose_name='Client'
        verbose_name_plural='Clients'

    def __str__(self):
        """Unicode representation of Client."""
        pass
