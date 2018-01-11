from django.db import models
from django.contrib.auth.models import AbstractUser as DjangoAbstractUser
from django.utils.translation import gettext_lazy as _


class PublicKeyCryptoMixin(models.Model):
    """Model mixin that adds fields to store an encrypted private key and
       it's corresponding public key."""

    enc_private_key = models.TextField(
        _('Encrypted Private Key'),
        help_text=_('Base64 encoded private key encrypted by a password '
                    'derived symmetric key.'))

    public_key = models.TextField(
        _('Public Key'),
        help_text=_('Base64 encoded public key'))

    class Meta:
        abstract = True


class User(PublicKeyCryptoMixin, DjangoAbstractUser):
    """User model that supports storing the user's encrypted private key and
       it's corresponding public key"""
