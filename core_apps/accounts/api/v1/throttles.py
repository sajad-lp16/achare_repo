from django.core.cache import cache
from django.conf import settings

from rest_framework.request import Request

from core_apps.utils.ip_tools import get_client_ip


class BaseThrottle:
    cache_timeout: int
    request_limit: int
    cache_key_template: str

    @classmethod
    def _is_allowed(cls, cache_key: str) -> bool:
        rate = cache.get(cache_key) or 0
        return rate >= cls.request_limit

    @classmethod
    def _update_request_rate(cls, cache_key: str) -> None:
        rate = (cache.get(cache_key) or 0) + 1
        cache.set(cache_key, rate, cls.cache_timeout)

    @classmethod
    def check(cls, request: Request) -> bool:
        ip = get_client_ip(request)
        cache_key = cls.cache_key_template.format(ip=ip)

        if cls._is_allowed(cache_key):
            return False

        cls._update_request_rate(cache_key)
        return True


class LoginRequestThrottle(BaseThrottle):
    cache_timeout = settings.LOGIN_REQUEST_BLOCK_TIMEOUT_SECONDS
    request_limit = settings.MAXIMUM_ALLOWED_LOGIN_REQUESTS
    cache_key_template = 'ip_{ip}_login_request'


class RegisterThrottle(BaseThrottle):
    cache_timeout = settings.REGISTER_REQUEST_BLOCK_TIMEOUT_SECONDS
    request_limit = settings.MAXIMUM_ALLOWED_REGISTER_REQUESTS
    cache_key_template = 'ip_{ip}_register'


class LoginThrottle(BaseThrottle):
    cache_timeout = settings.LOGIN_REQUEST_BLOCK_TIMEOUT_SECONDS
    request_limit = settings.MAXIMUM_ALLOWED_LOGIN_REQUESTS
    cache_key_template = 'ip_{ip}_login'
