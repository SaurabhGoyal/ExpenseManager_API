from django.contrib.auth import get_user_model
from rest_framework import serializers as rest_serializers
from rest_framework.exceptions import ValidationError

from apps.account import models as account_models


class UserSerializer(rest_serializers.ModelSerializer):
    """
    Serializer for User model having fields 'id', 'email', 'first_name', 'last_name' and 'phone'
    """
    confirm_password = rest_serializers.CharField(write_only=True)

    def validate(self, attrs):
        confirm_password = attrs.get('confirm_password')
        password = attrs.get('password')
        if confirm_password != password:
            raise ValidationError(u'Given passwords don\'t match.')
        return attrs

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'password', 'confirm_password', 'first_name', 'last_name', 'phone', )
        write_only_fields = ('password', 'confirm_password', )
        read_only_fields = ('id', )

    def create(self, validated_data):
        return get_user_model().objects.create_user(email=validated_data['email'], password=validated_data['password'],
                                                    first_name=validated_data['first_name'], last_name=validated_data.get('last_name', ''),
                                                    phone=validated_data.get('phone', ''))


class ExpiringTokenSerializer(rest_serializers.ModelSerializer):
    """
    Serializer for ExpiringToken model having field 'token' and fields of User
    """

    user = UserSerializer()
    token = rest_serializers.SerializerMethodField()

    def get_token(self, instance):
        return instance.key

    class Meta:
        model = account_models.ExpiringToken
        fields = ('token', 'user', )
