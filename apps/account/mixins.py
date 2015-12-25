from apps.account import permissions as account_permissions


class AnonymousOnlyMixin(object):
    """
    Mixin to ensure a view is accessible only by anonymous users.
    """

    authentication_classes = []
    # Todo: find a way to implement this perfectly
    permission_classes = [account_permissions.AnonymousOnlyPermission]
