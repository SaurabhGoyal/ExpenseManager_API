import datetime

from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import ugettext as _

from rest_framework.authtoken.models import Token


class UserManager(BaseUserManager):
    """ Extending to override account creation feature with email instead of username"""

    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError(_('User must have an email address'))

        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.create_user(email=email, password=password, **kwargs)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """ Extending to use email as the USERNAME field """

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True, verbose_name='Active')
    is_staff = models.BooleanField(default=False, verbose_name='Staff')
    phone = models.CharField(max_length=16, blank=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    def get_full_name(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

    def __unicode__(self):
        return _('{0}({1})'.format(self.get_full_name(), self.email))


class TokenManager(models.Manager):
    """
    Overrides to always provide a pre-fetched related 'user' for ExpiringToken.
    """
    def get_queryset(self):
        return super(TokenManager, self).get_queryset().select_related('user')


class ExpiringToken(Token):
    """
    Token that expires after a set time. Overrides Token from rest_framework to add validation using expiry time.
    """
    expiry_time = models.DateTimeField(default=datetime.datetime.now)

    objects = TokenManager()

    def __unicode__(self):
        return self.key

    def is_valid_token(self):
        return datetime.datetime.now() < self.expiry_time

    def invalidate_token(self):
        self.expiry_time = datetime.datetime.now()
        self.save()

    def validate_token(self):
        self.expiry_time = datetime.datetime.now() + datetime.timedelta(seconds=settings.WEB_SESSION_EXPIRY)
        self.save()

    def restore_token_life(self):
        new_expiry_time = datetime.datetime.now() + datetime.timedelta(seconds=settings.WEB_SESSION_EXPIRY)
        if self.expiry_time < new_expiry_time:
            self.expiry_time = new_expiry_time
            self.save()


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        ExpiringToken.objects.create(user=instance)