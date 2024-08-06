from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers

from core_apps.utils.otp_service import OTPService

User = get_user_model()


class LoginRequestSerializer(serializers.Serializer):
    phone_number = serializers.CharField(required=True)


class EnableUserSerializer(serializers.ModelSerializer):
    code = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('phone_number', 'password', 'code', 'first_name', 'last_name', 'email')

        extra_kwargs = {'password': {'write_only': True}}

    def validate_password(self, value: str):
        validate_password(value)
        return value

    def validate(self, attrs):
        phone_number = attrs.get('phone_number', '')
        code = attrs.get('code', '')

        if not OTPService.check_code(phone_number, code):
            raise serializers.ValidationError({'code': 'invalid or expired code!'})

        return attrs

    def update(self, instance: User, validated_data: dict):
        instance.is_active = True
        password = validated_data.pop('password')
        instance.set_password(password)
        return super().update(instance, validated_data)
