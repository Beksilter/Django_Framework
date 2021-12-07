from django.urls import path

from admins.views import UserListView, UserCreateView, UserUpdateView, UserDeleteView, CategoryListView, \
    CategoryCreateView, CategoryDeleteView, CategoryUpdateView, IndexTemplateView, ProductsListView, ProductsCreateView, \
    ProductsUpdateView, ProductsDeleteView

app_name = 'admins'
urlpatterns = [

    path('', IndexTemplateView.as_view(), name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('users-create/', UserCreateView.as_view(), name='admin_users_create'),
    path('users-update/<int:pk>', UserUpdateView.as_view(), name='admin_users_update'),
    path('users-delete/<int:pk>', UserDeleteView.as_view(), name='admin_users_delete'),

    path('category/', CategoryListView.as_view(), name='admin_category'),
    path('category/create/', CategoryCreateView.as_view(), name='admin_category_create'),
    path('category-delete/<int:pk>/', CategoryDeleteView.as_view(), name='admin_category_delete'),
    path('category-update/<int:pk>/', CategoryUpdateView.as_view(), name='admin_category_update'),
    # управление товарами
    path('product/', ProductsListView.as_view(), name='admin_product'),
    path('products-create/', ProductsCreateView.as_view(), name='admin_products_create'),
    path('products-update/<int:pk>/', ProductsUpdateView.as_view(), name='admin_products_update'),
    path('products-delete/<int:pk>/', ProductsDeleteView.as_view(), name='admin_products_delete'),


]
