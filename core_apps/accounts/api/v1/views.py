from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework import generics
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from core_apps.utils.otp_service import OTPService

from core_apps.accounts.utils.validators import is_valid_phone_number
from core_apps.accounts.api.v1.throttles import (
    LoginRequestThrottle,
    LoginThrottle,
    RegisterThrottle,
)
from core_apps.accounts.api.v1.serializers import (
    EnableUserSerializer,
    LoginRequestSerializer
)
from core_apps.accounts.api.v1.response_managers import (
    LoginRequestResponseManager,
    RegisterResponseManager,
    LoginResponseManager,
)

User = get_user_model()


class LoginRequestAPIView(generics.CreateAPIView):
    serializer_class = LoginRequestSerializer
    permission_classes = [AllowAny]
    throttle_manager = LoginRequestThrottle()
    response_manager = LoginRequestResponseManager()

    def post(self, request: Request, *args, **kwargs) -> Response:
        phone_number = request.data.get('phone_number', '')
        if not is_valid_phone_number(phone_number):
            return self.response_manager.get_invalid_phone_number_response()

        if not self.throttle_manager.check(request):
            return self.response_manager.get_throttle_response()

        user = User.objects.filter(phone_number=phone_number).first()
        if user is not None:
            if user.is_active:
                return self.response_manager.get_login_step_response()
        else:
            User.objects.create_inactive_user(phone_number=phone_number)

        OTPService.send_otp(phone_number)
        return self.response_manager.get_register_step_response()


class RegisterView(generics.UpdateAPIView):
    serializer_class = EnableUserSerializer
    throttle_manager = RegisterThrottle()
    permission_classes = [AllowAny]
    response_manager = RegisterResponseManager()
    http_method_names = ['patch']

    def patch(self, request: Request, *args, **kwargs) -> Response:
        phone_number = request.data.get('phone_number', '')
        if not is_valid_phone_number(phone_number):
            return self.response_manager.get_invalid_phone_number_response()

        if not self.throttle_manager.check(request):
            return self.response_manager.get_throttle_response()

        user = User.objects.filter(phone_number=phone_number).first()
        if user is None:
            return self.response_manager.get_not_found_response()

        if user.is_active:
            return self.response_manager.get_already_registered_response()

        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return self.response_manager.get_register_ok_response(data=serializer.data)


class LoginView(TokenObtainPairView):
    permission_classes = AllowAny,
    throttle_manager = LoginThrottle()
    response_manager = LoginResponseManager()

    def post(self, request: Request, *args, **kwargs) -> Response:
        phone_number = request.data.get('phone_number', '')
        if not is_valid_phone_number(phone_number):
            return self.error_response

        if not self.throttle_manager.check(request):
            return self.response_manager.get_throttle_response()

        response_body = super().post(request, *args, **kwargs).data
        return self.response_manager.get_login_ok_response(data=response_body)
