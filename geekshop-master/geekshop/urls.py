"""geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# include нужен дял того чтобы подключить urls.py из products

#' это не тот сеттингс что лежит в этойже папке! этот шире и тот в этот входит!
from django.conf import settings
from django.conf.urls.static import static

from products.views import index
#from products.views import products


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('products/', include('products.urls', namespace='products'), name='products'), # это объявлене глобального адреса который стал пространством имен. и берется он из urls из папки products
    path('users/', include('users.urls', namespace='users'), name='users'),
    path('baskets/', include('baskets.urls', namespace = 'baskets'), name='baskets'),
    path('admins/', include('admins.urls', namespace = 'admins'), name='admins'),
    
]
'''
здесь путь внутри пространств адресов образуется путем сложения стрингов. Например "users/" и следующего 
("register/") в этом пути можно ообще написать все что угодно, если что...
слеш работает как разделитель для восприятяи человеком (можно и без него), а если его не будет то адреса будут типа «userslogin»
'''

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)


