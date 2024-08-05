import random

from django.core.cache import cache
from django.conf import settings


class OTPService:
    LOGIN_REQUEST_CACHE_KEY = 'otp_login_code_user_{phone_number}'

    @staticmethod
    def _generate_otp_code():
        return random.randint(100000, 999999)

    @classmethod
    def _set_code(cls, cache_key: str, otp_code: str | int) -> None:
        cache.set(cache_key, otp_code, settings.OTP_TIMEOUT_SECONDS)

    @classmethod
    def _code_matches(cls, cache_key: str, otp_code: str | int) -> bool:
        stored_key = cache.get(cache_key, '')
        return str(stored_key) == str(otp_code)

    @classmethod
    def _send_otp(cls, phone_number: str, otp_code: str | int) -> None:
        # Send operation!
        return

    @classmethod
    def check_code(cls, phone_number: str, otp_code: str | int) -> bool:
        cache_key = cls.LOGIN_REQUEST_CACHE_KEY.format(phone_number=phone_number)
        if not cls._code_matches(cache_key, otp_code):
            return False
        return True

    @classmethod
    def send_otp(cls, phone_number: str) -> None:
        cache_key = cls.LOGIN_REQUEST_CACHE_KEY.format(phone_number=phone_number)
        otp_code = cls._generate_otp_code()

        print(otp_code)  # for test scenario

        cls._set_code(cache_key, otp_code)
        cls._send_otp(phone_number, otp_code)
