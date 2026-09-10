from users.models import CustomUser
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions


class CustomUserSerializer(ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ['email','username', 'first_name', 'last_name', 'created_date', 'updated_date']


class AdminUserSerializer(ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ['id','email','username', 'is_active', 'is_staff', 'is_superuser', 'first_name', 'last_name', 'created_date', 'updated_date']
        read_only_fields = ['id', 'created_date', 'updated_date']

class RegistrationSerializer(ModelSerializer):
    password = serializers.CharField(max_length=255, min_length=8, write_only=True)
    password1 = serializers.CharField(max_length=255, min_length=8, write_only=True)

    class Meta:
        model = CustomUser
        fields = ["email","username", "password", "password1"]

    def validate(self, attrs):
        if attrs.get("password") != attrs.get("password1"):
            raise serializers.ValidationError(
                {"detail": "passwords doesn't match"})

        try:
            validate_password(attrs.get("password"))
        except exceptions.ValidationError as e:
            raise serializers.ValidationError(
                {"password": list(e.messages)})
        return super().validate(attrs)

    def create(self, validated_data):
        validated_data.pop("password1", None)
        return CustomUser.objects.create_user(**validated_data)


class ChangePasswordSerializer(serializers.Serializer):

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    new_password1 = serializers.CharField(required=True)


    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):  # <-- اینجا استفاده می‌شه
            raise serializers.ValidationError("old password is wrong")
        return value
    
    
    def validate(self, attrs):
        if attrs.get("new_password") != attrs.get("new_password1"):
            raise serializers.ValidationError(
                {"detail": "passwords doesn't match"})
        try:
            validate_password(attrs.get("new_password"))
        except exceptions.ValidationError as e:
            raise serializers.ValidationError(
                {"new_password": list(e.messages)})
        return super().validate(attrs)