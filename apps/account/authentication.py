from django.contrib.auth import get_user_model

from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import APIException, AuthenticationFailed

from apps.account import models as account_models


class TokenExpiredException(APIException):
    """
    Overrides APIException to provide custom detail and status_code
    """
    status_code = 420
    default_detail = u'Token expired.'


class ExpiringTokenAuthentication(TokenAuthentication):
    """
    Custom token based authentication , Override from the basic rest_authentication.TokenAuthentication Class
    Token validation condition is added to the default authenticate_credentials function
    Default Token model is also changed to the accounts.Token Model
    """
    model = account_models.ExpiringToken

    def authenticate_credentials(self, key):

        token = self.model.objects.filter(key=key).first()
        if token:
            if not token.user.is_active:
                raise AuthenticationFailed(u'User inactive or deleted')

            if token.is_valid_token():
                token.restore_token_life()
            else:
                raise TokenExpiredException()
            return get_user_model().objects.get(pk=token.user.id), token

        raise AuthenticationFailed(u'Invalid token')
