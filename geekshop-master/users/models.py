from django.db import models
from django.contrib.auth.models import AbstractUser
# Импортировали абстрактного пользователя потому что нужно от него наследоваться с целью расширения (добавим картинку)

# Проба пера с валидатором
def OnlyRusText(value):
    """
    Типа «мой собственный» валидатор, который не пропускает строки с английскими буквами и с заглавными
    PS: понимаю что можно было по-другому и догадываюсь что что-то софункциональное уже естьв Django
    но попросили создать валидатор с нуля....
    И он работает… хоть и алгорим дубовый... ничего умней в голову почему-то не пришло…
    """
    from django.core.exceptions import ValidationError
    def match(text):
        alphabet=set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
        for i in text:
            if i not in alphabet: return False
        return True

    if not match(value):
        raise ValidationError('%s ЭТО НЕ РУССКИЙ ТЕКСТ!' % value)

# модель пользователей
class Users(AbstractUser):
    image = models.ImageField(blank=True, upload_to='users_images')
# отключил валидатор из 5*(4) задания. чтобы не мешался.
#    first_name = models.CharField(max_length=25, validators=[OnlyRusText]) # Это нужно удалить
#    last_name = models.CharField(max_length=25, validators=[OnlyRusText]) # Это тоже нужно удалить