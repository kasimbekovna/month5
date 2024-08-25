from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from .models import ConfirmationCode


class UserAuthSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserCreateSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            raise ValidationError('User already exists!')
        return username


    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            is_active=False
        )
        ConfirmationCode.objects.create(user=user)
        return user


class ConfirmationSerializer(serializers.Serializer):
    username = serializers.CharField()
    code = serializers.CharField(max_length=6)

    def validate(self, data):
        try:
            user = User.objects.get(username=data['username'])
        except User.DoesNotExist:
            raise ValidationError("User does not exist")

        try:
            confirmation_code = ConfirmationCode.objects.get(user=user, code=data['code'])
        except ConfirmationCode.DoesNotExist:
            raise ValidationError("Invalid confirmation code")

        return data

    def save(self):
        data = self.validated_data
        user = User.objects.get(username=data['username'])
        user.is_active = True
        user.save()
        ConfirmationCode.objects.get(user=user).delete()
        return user