from datetime import datetime, timedelta

from django.core.exceptions import ValidationError
from rest_framework import serializers

from .models import User


class CreateUserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(
        min_length=5, max_length=50, required=True)
    email = serializers.CharField(min_length=6, required=True)
    password = serializers.CharField(
        min_length=8, write_only=True, required=True)

    class Meta:
        model = User
        fields = ('full_name', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = self.Meta.model(**validated_data)
        if password is not None:
            user.set_password(password)
        user.save()
        return user


class ConfigUserSerializer(serializers.ModelSerializer):
    notifications_count = serializers.SerializerMethodField(
        "get_unread_notifications")
    # birthday = serializers.DateField(format="%d %B %Y")

    class Meta:
        model = User
        fields = ('full_name', 'email', 'profile_img_url', 'birthday', 'gender',
                  'phone_number', 'recovery_email', 'is_email_verified', 'notifications_count', 'last_password_change_at', 'is_two_factor_auth_enabled')

    def get_unread_notifications(self, obj):
        return len(obj.notification_set.filter(is_read=False))


class UpdateUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('full_name', 'profile_img_url',
                  'birthday', 'gender', 'recovery_email', 'phone_number', 'is_two_factor_auth_enabled')

    def validate(self, data):
        if hasattr(self, 'initial_data'):
            unknown_keys = set(self.initial_data.keys()) - \
                set(self.fields.keys())
            if unknown_keys:
                raise ValidationError(
                    "Got unknown fields: {}".format(unknown_keys))
        return data
