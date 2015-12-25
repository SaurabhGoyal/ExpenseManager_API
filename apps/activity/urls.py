from django.conf.urls import include, patterns, url
from rest_framework import routers
from apps.activity import views as activity_views


router = routers.SimpleRouter()
router.register(r'', activity_views.UserActivityViewSet, 'user_activities')


# See: https://docs.djangoproject.com/en/dev/topics/http/urls/
urlpatterns = patterns(
    '',
    url(r'user-activities', include(router.urls)),
)
