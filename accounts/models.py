from django.contrib.auth.models import User
from accounts.utils import resize_image
from justice_law_office.constants import GENDERS, VILLES
from django.db import models
from django.db.models.base import Model
from embed_video.fields import EmbedVideoField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Avocat(models.Model):
    
    adresse = models.CharField(max_length=255, blank=True, null=True)
    sexe = models.CharField(max_length=1, blank=True,
                            null=True, choices=GENDERS, default='M')
                            
    immeuble = models.CharField(max_length=255, blank=True, null=True)
    quartier = models.CharField(max_length=255, blank=True, null=True)
    indication = models.CharField(max_length=255, blank=True, null=True)
    ville = models.CharField(max_length=150, blank=True,
                             null=True, choices=VILLES)
    zip_code = models.IntegerField(blank=True, null=True)
    tel = models.CharField(max_length=255, blank=True, null=True)
    gsm = models.CharField(max_length=255, blank=True, null=True)
    presentation = models.TextField(blank=True, null=True)
    education = models.TextField(blank=True, null=True)
    experience = models.TextField(blank=True, null=True)
    competence = models.TextField(blank=True, null=True)  # Compétence
    rib = models.CharField(max_length=255, blank=True, null=True)
    instagram = models.CharField(max_length=255, blank=True, null=True)
    youtube = models.CharField(max_length=255, blank=True, null=True)
    facebook = models.CharField(max_length=255, blank=True, null=True)
    web = models.CharField(max_length=255, blank=True, null=True)
    video = EmbedVideoField(blank=True, null=True)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        print("this is my image :", self.profile_image)
        if self.profile_image and self.profile_image != '/uploads/default.png':
            img = resize_image(self.profile_image.path, (471, 470), Mode.ZOOM)
            img.save(self.profile_image.path, quality=100)
    

    class Meta:
        db_table = 'avocat'
        verbose_name = _("Avocat")
        verbose_name_plural = _("Avocats")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("attorney_detail", kwargs={"pk": self.pk})
