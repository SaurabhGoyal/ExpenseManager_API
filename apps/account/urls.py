from django.conf.urls import patterns, url
from apps.account import views as account_views

# See: https://docs.djangoproject.com/en/dev/topics/http/urls/
urlpatterns = patterns(
    '',
    url(r'^login/$', account_views.LoginView.as_view(), name='login'),
    url(r'^register/$', account_views.RegistrationView.as_view(), name='register'),
)
