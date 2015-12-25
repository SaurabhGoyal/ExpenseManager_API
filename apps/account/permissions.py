from rest_framework import permissions as rest_permissions


class AnonymousOnlyPermission(rest_permissions.BasePermission):
    """
    Permission to ensure a view is accessible only by an anonymous user
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_anonymous()
