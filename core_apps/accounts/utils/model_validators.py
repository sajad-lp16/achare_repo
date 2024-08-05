from django.core.exceptions import ValidationError

from core_apps.accounts.utils.validators import is_valid_phone_number


def phone_number_validator(value: str) -> None:
    if not is_valid_phone_number(value):
        raise ValidationError(f'{value} is not a valid phone number')
