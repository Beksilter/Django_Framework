from django.contrib import admin
from users.models import Users

#admin.site.register(Users) # если оставить, то не даст модифицировать вывод через класс

#модификация стандартной админки
@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    # табличный вывод (как каталога)
    list_display=('username', 'first_name','last_name', 'email','is_staff', 'is_active', 'is_superuser')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    fields = (('username', 'email'),('is_staff', 'is_active', 'is_superuser'),('first_name','last_name'), 'image', 'password')
    
