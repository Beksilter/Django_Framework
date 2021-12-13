
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView

from admins.forms import UserAdminRegisterForm, UserAdminProfileForm, CategoryUpdateFormAdmin, ProductsForm, ProductUpdate
from authapp.models import User
from mainapp.mixin import BaseClassContextMixin, CustomDispatchMixin
from mainapp.models import ProductCategory, Product

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy


class IndexTemplateView(TemplateView):
    template_name = 'admins/admin.html'


# Список пользователей

class UserListView(ListView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-read.html'
    title = 'Админка | Пользователи'


class UserCreateView(CreateView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-create.html'
    form_class = UserAdminRegisterForm
    success_url = reverse_lazy('admins:admin_users')
    title = 'Админка | Создать пользователя'


class UserUpdateView(UpdateView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users')
    title = 'Админка | Обновить пользователя'


class UserDeleteView(DeleteView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users')
    title = 'Админка | Удалить пользователя'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


# Category
class CategoryListView(ListView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-category-read.html'
    title = 'Админка | Список категорий'


class CategoryDeleteView(DeleteView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-category-update-delete.html'
    success_url = reverse_lazy('admins:admin_category')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_active:
            self.object.is_active = False
        else:
            self.object.is_active = True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class CategoryCreateView(CreateView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-category-create.html'
    success_url = reverse_lazy('admins:admin_category')
    form_class = CategoryUpdateFormAdmin
    title = 'Админка | Создание категории'


class CategoryUpdateView(UpdateView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-category-update-delete.html'
    form_class = CategoryUpdateFormAdmin
    title = 'Админка | Обновления категории'
    success_url = reverse_lazy('admins:admin_category')


# Товары
class ProductsListView(ListView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'admins/admin-products-read.html'
    title = 'Админка | Список товаров'


class ProductsCreateView(CreateView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'admins/admin-products-create.html'
    form_class = ProductsForm
    success_url = reverse_lazy('admins:admins_product')
    title = 'Админка | Создание товаров'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = 'GeekShop - новый товар CBV'
        return context


class ProductsUpdateView(UpdateView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'admins/admin-products-update-delete.html'
    form_class = ProductUpdate
    title = 'Админка | Обновления товаров'
    success_url = reverse_lazy('admins:admins_product')



class ProductsDeleteView(DeleteView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'admins/admin-products-read.html'
    success_url = reverse_lazy('admins:admins_product')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False if self.object.is_active else True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
