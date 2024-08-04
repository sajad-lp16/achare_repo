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

    def create_user(self, **user_data):
        user = self._perform_save_user(**user_data)

        user.save(using=self._db)
        return user

    def create_inactive_user(self, **user_data):
        user = self._perform_save_user(**user_data)
        user.is_active = False
        user.save(using=self._db)
        return user

    def create_superuser(self, **user_data):
        user = self._perform_save_user(**user_data)

        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user

    def active_users(self):
        return self.get_queryset().filter(active=True)

    def inactive_users(self):
        return self.get_queryset().filter(active=False)
