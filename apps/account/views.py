from rest_framework.authtoken import views
from rest_framework.response import Response

from apps.account import (
    models as account_models,
    serializers as account_serializers,
)


class LoginView(views.ObtainAuthToken):
    """
    Overrides to validate token after creation.
    """
    http_method_names = ['post']

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = account_models.ExpiringToken.objects.get_or_create(user=user)

        # Validate the token
        token.validate_token()

        # Return data of validated token
        return Response(account_serializers.ExpiringTokenSerializer(token).data)
