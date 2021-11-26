from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.
def NoSymbolsInName(value):
    """
    Валидатор проверяет имя и фамилию на отсутствие символов.
    """
    def match(text):
        symbols=set('"~!@#$%^&*()+`";:<>/\|')
        for i in text:
            if i in symbols: return False
        return True
    if match(value):
        raise ValidationError('Введены недопустимые символы!' % value)






class User(AbstractUser):
    image=models.ImageField(upload_to='users_image', blank=True)
    age=models.PositiveIntegerField(default=18)
    first_name = models.CharField(max_length=25, validators=[NoSymbolsInName])  # Это нужно удалить
    last_name = models.CharField(max_length=25, validators=[NoSymbolsInName])  # Это тоже нужно удалить





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