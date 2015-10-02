from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import ugettext as _


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

    def get_full_name(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

    def __unicode__(self):
        if self.is_admin:
            return _("{0} (Admin)".format(self.email))
        return _("{0} (User)".format(self.email))
