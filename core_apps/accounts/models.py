from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    phone_number = models.CharField(verbose_name=_('phone number'), max_length=15, unique=True, db_index=True)


    class Meta:
        verbose_name = _('User')
        verbose_name = _('Users')
        db_table = 'users'
