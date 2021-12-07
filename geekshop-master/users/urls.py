"""
это модуль обеспечивающий работу пространства адресов приложения users
"""
from django.urls import path
from users.views import login, registration, logout, profile

app_name = 'users' # без этого не сработает include там где подключается пространство адресов.

urlpatterns = [
    path('login/', login, name = 'login'),
    path('registration/', registration, name = 'registration'),
    path('logout/', logout, name= 'logout'),
    path('profile/', profile, name='profile'),
]


