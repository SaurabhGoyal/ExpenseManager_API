from rest_framework import serializers as rest_serializers

from apps.account import models as account_models

class UserSerializer(rest_serializers.ModelSerializer):
    """
    Serializer for User model having fields 'id', 'email', 'first_name', 'last_name' and 'phone'
    """

    class Meta:
        model = account_models.User
        fields = ('id', 'email', 'first_name', 'last_name', 'phone', )


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