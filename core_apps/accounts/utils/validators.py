import re


def is_valid_phone_number(phone_number: str) -> bool:
    '''simple regex NOT SUITABLE FOR PRODUCTION !!!'''
    pattern = r'^09[\d]{9}'

    if re.match(pattern, phone_number) is None:
        return False
    return True
