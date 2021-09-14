
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext as _
from accounts.utils import CITIES, Mode, WEEK_DAYS, get_time_range, resize_image
from embed_video.fields import EmbedVideoField
import pandas as pd
# Create your models here.

TIMES = get_time_range(start='00:00:00', end='23:59:59', freq='15T')


# class AttorneyManager(UserManager):

#     def get_queryset(self, *args, **kwargs):
#         print("AttorneyManager kwargs : ", kwargs)
#         queryset = super().get_queryset(*args, **kwargs).filter(type=Types.ATTORNEY)

#         print("AttorneyManager queryset : ", queryset)
#         return queryset


class Types(models.TextChoices):
    ATTORNEY = 'attorney'
    CLIENT = 'client'


class Attorney(AbstractUser):
    choices = (
        ('H', _('Homme')),
        ('F', _('Femme')),
    )

    #objects = AttorneyManager()

    type = models.CharField(_('Type'), max_length=50,
                            default=Types.ATTORNEY, null=True, blank=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True,
                           null=True, choices=choices, default='H')
    building = models.CharField(max_length=255, blank=True, null=True)
    neighborhood = models.CharField(max_length=255, blank=True, null=True)
    indication = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=150, blank=True,
                            null=True, choices=CITIES)
    zip_code = models.IntegerField(blank=True, null=True)
    tel = models.CharField(max_length=255, blank=True, null=True)
    gsm = models.CharField(max_length=255, blank=True, null=True)
    presentation = models.TextField(blank=True, null=True)
    education = models.TextField(blank=True, null=True)
    experience = models.TextField(blank=True, null=True)
    skill = models.TextField(blank=True, null=True)  # Compétence
    rib = models.CharField(max_length=255, blank=True, null=True)
    instagram = models.CharField(max_length=255, blank=True, null=True)
    youtube = models.CharField(max_length=255, blank=True, null=True)
    facebook = models.CharField(max_length=255, blank=True, null=True)
    web = models.CharField(max_length=255, blank=True, null=True)
    video = EmbedVideoField(blank=True, null=True)
    profile_image = models.ImageField(
        upload_to='uploads/%Y/%m/%d/', default='/uploads/default.png', blank=True, null=True, max_length=255)
    # client_type = models.CharField(max_length=100, blank=True, null=True, choices=choices)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        print("this is my image :", self.profile_image)
        if self.profile_image and self.profile_image != '/uploads/default.png':
            img = resize_image(self.profile_image.path, (471, 470), Mode.ZOOM)
            img.save(self.profile_image.path, quality=100)

    class Meta:
        db_table = 'attorney'
        managed = True
        verbose_name = 'Attorney'
        verbose_name_plural = 'Attorneys'


class City(models.Model):

    name = models.CharField(max_length=150, blank=True,
                            null=True, choices=CITIES)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'city'
        managed = True
        verbose_name = 'City'
        verbose_name_plural = 'Cities'


class Schedule(models.Model):

    day_name = models.CharField(
        max_length=100, blank=True, null=True, choices=WEEK_DAYS)
    time_from = models.CharField(
        max_length=10, blank=True, null=True, choices=TIMES)
    time_to = models.CharField(
        max_length=10, blank=True, null=True, choices=TIMES)
    attorney = models.ForeignKey(
        Attorney, on_delete=models.CASCADE, related_name='attorney', blank=True, null=True)

    def __str__(self):
        return self.day_name

    class Meta:
        db_table = 'schedule'
        managed = True
        verbose_name = 'Schedule'
        verbose_name_plural = 'Schedules'
