from rest_framework.authtoken import views as authtoken_views
from rest_framework import (
    generics as rest_generics,
    response as rest_response,
)

from apps.account import (
    mixins as account_mixins,
    models as account_models,
    serializers as account_serializers,
)


class LoginView(account_mixins.AnonymousOnlyMixin, authtoken_views.ObtainAuthToken):
    """
    API to login an existing user.
    """
    http_method_names = ['post']

    def post(self, request):
        """
        Overrides to validate token after creation.
        """

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = account_models.ExpiringToken.objects.get_or_create(user=user)

        # Validate the token
        token.validate_token()

        # Return data of validated token
        return rest_response.Response(account_serializers.ExpiringTokenSerializer(token).data)


class RegistrationView(account_mixins.AnonymousOnlyMixin, rest_generics.CreateAPIView):
    """
    API to register a new user.
    """
    http_method_names = ['post']
    serializer_class = account_serializers.UserSerializer
