from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
from datetime import timedelta
from django.dispatch import receiver
# Create your models here.
from django.db.models.signals import post_save
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


class UserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'W'

    GENDER_CHOICES = (
        (MALE, 'М'),
        (FEMALE, 'Ж'),
    )

    user = models.OneToOneField(User, unique=True, null=False, db_index=True, on_delete=models.CASCADE)
    about = models.TextField(verbose_name='о себе', blank=True, null=True)
    gender = models.CharField(verbose_name='пол', choices=GENDER_CHOICES, blank=True, max_length=2)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.userprofile.save()









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
