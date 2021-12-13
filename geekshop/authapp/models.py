from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
from datetime import timedelta

# Create your models here.
from django.utils.timezone import now

class User(AbstractUser):
    image = models.ImageField(upload_to='users_image', blank=True)
    age = models.PositiveIntegerField(default=18)

    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(auto_now=True, blank=True, null=True)

    def is_activation_key_expires(self):
        if now () <= self.activation_key_expires + timedelta(hours=48):
            return False
        return True


# def validate_password_strength(value):
#     """Validates that a password is as least 10 characters long and has at least
#     2 digits and 1 Upper case letter.
#     """
#     min_length = 6
#
#     if len(value) < min_length:
#         raise ValidationError(_('Password must be at least {6} characters '
#                                 'long.').format(min_length))
#
#     # check for 1 digits
#     if sum(c.isdigit() for c in value) < 1:
#         raise ValidationError(_('Password must container at least 1 digits.'))
#
#     # check for uppercase letter
#     if not any(c.isupper() for c in value):
#         raise ValidationError(_('Password must container at least 1 uppercase letter.'))
#
#     return value
