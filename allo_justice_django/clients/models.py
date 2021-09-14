
from accounts.models import Attorney, Types
from datetime import datetime
from django.contrib.auth import password_validation
from django.contrib.auth.base_user import AbstractBaseUser
from django.db.models.fields import proxy
from django.utils import timezone
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext as _
from accounts.utils import CITIES, Mode, WEEK_DAYS, get_time_range, resize_image
import pandas as pd

# Create your models here.


# class ClientManager(UserManager):
#     def get_queryset(self, *args, **kwargs):
#         queryset = super().get_queryset(*args, **kwargs).filter(type=Attorney.Types.CLIENT)
#         return queryset


class Client(Attorney):

    # objects = ClientManager()

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = Types.CLIENT
        return super().save(*args, **kwargs)

    class Meta:
        db_table = 'client'
        managed = True
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
