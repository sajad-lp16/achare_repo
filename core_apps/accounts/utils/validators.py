import re

from django.core.exceptions import ValidationError

def phone_number_validator(value):
    '''simple regex NOT SUITABLE FOR PRODUCTION !!!'''
    pattern = r'^09[\d]{9}'

    if re.match(pattern, value) is None:
        raise ValidationError(f'{value} is not a valid phone number')