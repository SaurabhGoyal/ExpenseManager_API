from django.contrib import admin
from django.conf.urls import patterns, include, url

# See: https://docs.djangoproject.com/en/dev/ref/contrib/admin/#hooking-admin-site-instances-into-your-urlconf
admin.autodiscover()

# See: https://docs.djangoproject.com/en/dev/topics/http/urls/
urlpatterns = patterns('',

                       url(r'^api/account/', include('apps.account.urls', namespace="account")),
                       url(r'^api/activity/', include('apps.activity.urls', namespace="activity")),
                       url(r'^admin/', include(admin.site.urls)),

)
