"""
это модуль обеспечивающий работу пространства адресов приложения products
"""
from django.urls import path
from products.views import products

# from products.views import index # не записываем потому, что он включен в главный urls.py

app_name = 'products'

urlpatterns = [
    path('',products, name = 'index'), # но это уже index не от сайта а от пространства адресов products
    path('<int:category_id>/',products, name = 'category'), # адрес будет ../category/<id> (исправил опечатку - не было разделителя, работет адреса формировались без него
    path('page/<int:page>/',products, name = 'page'), 
]


