from django.core.cache import cache
from django.conf import settings

from rest_framework.request import Request

from core_apps.utils.ip_tools import get_client_ip


class LoginRequestThrottle:
    def __init__(self):
        self.cache_timeout = settings.LOGIN_REQUEST_BLOCK_TIMEOUT_SECONDS
        self.request_limit = settings.MAXIMUM_ALLOWED_LOGIN_REQUESTS
        self.cache_key_template = 'ip_{ip}_login_request'

    def _is_allowed(self, cache_key: str) -> bool:
        rate = cache.get(cache_key) or 0
        return rate >= self.request_limit

    def _update_request_rate(self, cache_key: str) -> None:
        rate = (cache.get(cache_key) or 0) + 1
        cache.set(cache_key, rate, self.cache_timeout)

    def check(self, request: Request) -> bool:
        ip = get_client_ip(request)
        cache_key = self.cache_key_template.format(ip=ip)

        if self._is_allowed(cache_key):
            return False

        self._update_request_rate(cache_key)
        return True


class RegisterThrottle:
    def __init__(self):
        self.cache_timeout = settings.REGISTER_REQUEST_BLOCK_TIMEOUT_SECONDS
        self.request_limit = settings.MAXIMUM_ALLOWED_REGISTER_REQUESTS
        self.cache_key_template = 'ip_{ip}_register'

    def _is_allowed(self, cache_key: str) -> bool:
        rate = cache.get(cache_key) or 0
        return rate >= self.request_limit

    def _update_request_rate(self, cache_key: str) -> None:
        rate = (cache.get(cache_key) or 0) + 1
        cache.set(cache_key, rate, self.cache_timeout)

    def check(self, request: Request) -> bool:
        ip = get_client_ip(request)
        cache_key = self.cache_key_template.format(ip=ip)

        if self._is_allowed(cache_key):
            return False

        self._update_request_rate(cache_key)
        return True


class LoginThrottle:
    def __init__(self):
        self.cache_timeout = settings.LOGIN_REQUEST_BLOCK_TIMEOUT_SECONDS
        self.request_limit = settings.MAXIMUM_ALLOWED_LOGIN_REQUESTS
        self.cache_key_template = 'ip_{ip}_login'

    def _is_allowed(self, cache_key: str) -> bool:
        rate = cache.get(cache_key) or 0
        return rate >= self.request_limit

    def _update_request_rate(self, cache_key: str) -> None:
        rate = (cache.get(cache_key) or 0) + 1
        cache.set(cache_key, rate, self.cache_timeout)

    def check(self, request: Request) -> bool:
        if request.method != 'POST':
            return True

        ip = get_client_ip(request)
        cache_key = self.cache_key_template.format(ip=ip)

        if self._is_allowed(cache_key):
            return False

        self._update_request_rate(cache_key)
        return True
