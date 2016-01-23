from rest_framework import (
    viewsets as rest_viewsets,
)

from apps.activity import (
    models as activity_models,
    serializers as activity_serializers,
)


class UserActivityViewSet(rest_viewsets.ModelViewSet):
    """
    ViewSet to perform various operations on UserActivity model.
    """

    serializer_class = activity_serializers.UserActivitySerializer

    def get_queryset(self):
        return self.request.user.useractivity_set

    def create(self, request, *args, **kwargs):
        print self.request.user.id
        request.data[u'user'] = self.request.user.id
        return super(UserActivityViewSet, self).create(request, *args, **kwargs)
