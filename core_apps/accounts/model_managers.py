import random
import string

from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def _perform_save_user(self, **user_data):
        email = user_data.pop('email', None)
        password = user_data.pop('password', None)

        if email is not None:
            email = self.normalize_email(email)

        if not password:
            raise ValueError(_('user must have password'))

        validate_password(password)

        user = self.model(password=password, email=email, **user_data)
        user.set_password(password)

        return user

    def _get_random_password(self) -> str:
        return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

    def create_user(self, **user_data):
        user = self._perform_save_user(**user_data)

        user.save(using=self._db)
        return user

    def create_inactive_user(self, **user_data):
        password = self._get_random_password()
        user = self._perform_save_user(password=password, **user_data)
        user.is_active = False
        user.save(using=self._db)
        return user

    def update_user(self, user, **user_data):
        password = user_data.pop('password', None)
        first_name = user_data.pop('first_name', None)
        last_name = user_data.pop('last_name', None)
        email = user_data.pop('email', None)

        if email is not None:
            email = self.normalize_email(email)

        if not password:
            raise ValueError(_('user must have password'))

        validate_password(password)

        user.set_password(password)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save(using=self._db)

        return user

    def create_superuser(self, **user_data):
        user = self._perform_save_user(**user_data)

        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user
