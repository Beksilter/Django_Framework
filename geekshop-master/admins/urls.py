"""
это модуль обеспечивающий работу пространства адресов приложения «админка»
"""
from django.urls import path
from admins.views import index, admin_users_update, admin_users_delete, admin_categorys_delete, admin_categorys_update,  admin_products_update, admin_products_delete
# CBV
from admins.views import UserListView, UserCreateView, ProductCategoryListView, ProductsListView, ProductsCategoryCteateView, ProductsCreateView

app_name = 'admins'

urlpatterns = [
    path('', index, name = 'index'),
    # управление пользователями
    path('users/', UserListView.as_view(), name = 'admin_users'),
    path('users-create/', UserCreateView.as_view(), name = 'admin_users_create'),
    path('users-update/<int:pk>/', admin_users_update, name = 'admin_users_update'),
    path('users-delete/<int:pk>/', admin_users_delete, name = 'admin_users_delete'),
    # управление категориями
    path('categorys/', ProductCategoryListView.as_view(), name = 'admin_categorys'),
    path('categorys-create/', ProductsCategoryCteateView.as_view(), name = 'admin_categorys_create'),
    path('categorys-update/<int:key>/', admin_categorys_update, name = 'admin_categorys_update'),
    path('categirys-delete/<int:key>/', admin_categorys_delete, name = 'admin_categorys_delete'),
    # управление товарами 
    path('products/', ProductsListView.as_view(), name = 'admin_products'),
    path('products-create/', ProductsCreateView.as_view(), name = 'admin_products_create'),
    path('products-update/<int:key>/', admin_products_update, name = 'admin_products_update'),
    path('products-delete/<int:key>/', admin_products_delete, name = 'admin_products_delete'),
    
]
