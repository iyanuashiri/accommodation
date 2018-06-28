from django.db import models
from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail


from .managers import UserManager

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    is_tenant = models.BooleanField(default=False)
    is_landlord = models.BooleanField(default=False)

    email_address = models.EmailField(
        _('email address'),
        unique=True,
        error_messages={
            'unique': _("A user with that email address already exists."),
        })
    first_name = models.CharField(_('first name'), max_length=100)
    last_name = models.CharField(_('last name'), max_length=100)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email_address'
    REQUIRED_FIELDS = ['fullname', 'business_name']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        """
        Return the fullname
        """
        fullname = '{0} {1}'.format(self.first_name, self.last_name)
        return fullname

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email_address], **kwargs)


class Tenant(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        verbose_name = 'tenant'
        verbose_name_plural = 'tenants'

    def __str__(self):
        return self.user.fullname


class LandLord(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        verbose_name = 'landlord'
        verbose_name_plural = 'landlords'

    def __str__(self):
        return self.user.fullname
