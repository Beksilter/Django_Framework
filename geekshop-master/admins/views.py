from django.shortcuts import render, HttpResponseRedirect
from users.models import Users
from products.models import ProductsCategory, Products
from admins.forms import AdminsUserCreationForm, AdminsUserUpdateForm, AdminsCategoryElementForm, AdminsProductElementForm
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test
# для CBV
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

# Главная старница
@user_passes_test(lambda u: u.is_staff)
def index(request):
    context = {
        'title': 'Административная панель GeekShop',
    }
    return render(request, 'admins/index.html', context)
    
# 4 контроллера для CRUD
# Список пользователей

class UserListView(ListView): 
    model = Users
    template_name = 'admins/admin-users-read.html' 

    def get_context_data(self, *,object_list=None, **kwargs):
        context = super().get_context_data() 
        context['title'] = 'GeekShop - Пользователи CBV'     
        return context 

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self,request, *args, **kwargs):
        return super().dispatch(request,*args, **kwargs)


# @user_passes_test(lambda u: u.is_staff)
# def admin_users(request):
    # context = {
        # 'title': 'GeekShop - Пользователи',
        # 'users': Users.objects.all()
    # }
    # return render(request, 'admins/admin-users-read.html', context)
    
# Добавление пользователя

class UserCreateView(CreateView):
    model = Users
    template_name = 'admins/admin-users-create.html' 
    form_class = AdminsUserCreationForm
    success_url = reverse_lazy('admins:admin_users')

    def get_context_data(self, *,object_list=None, **kwargs):
        context = super().get_context_data() 
        context['title'] = 'GeekShop - Новый пользователь на основе CBV'     
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self,request, *args, **kwargs):
        return super().dispatch(request,*args, **kwargs)


# @user_passes_test(lambda u: u.is_staff)
# def admin_users_create(request):
    # if request.method == 'POST':
        # form=AdminsUserCreationForm(data=request.POST, files = request.FILES) # Важный момент с передачей файла!
        # if form.is_valid():
            # form.save()
            # # сообщение не нужно, поскольку в случае успеха мы перейдем на страницу с перечнем пользователей
            # return HttpResponseRedirect(reverse('admins:admin_users'))
        # # else:
            # # print(form.errors) # это мы вывели ошибки валидации формы в отладке
    # else:
        # form = AdminsUserCreationForm()
    
    # context = {
        # 'title': 'GeekShop - Новый пользователь',
        # 'form': form,
    # }
    # return render(request, 'admins/admin-users-create.html', context)

# Изменение пользователя
@user_passes_test(lambda u: u.is_staff)
def admin_users_update(request, pk):
    selected_user = Users.objects.get(id=pk) 
    # это тот пользователь на которого кликнули по ссылке на странице пользователей админки
    if request.method == 'POST':
        form = AdminsUserUpdateForm(instance = selected_user, data = request.POST) # сказали что менять будем у этого пользователя, которого выбрали на странице
        if form.is_valid(): 
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = AdminsUserUpdateForm(instance=selected_user) # передали текущего пользователя для отображания его «ТТХ» через GET запрос
    context = {
        'title': 'GeekShop - Изменение профиля пользователя',
        'form': form,
        'selected_user': selected_user,
    }
    return render(request, 'admins/admin-users-update-delete.html', context)

#удаление пользователя    
@user_passes_test(lambda u: u.is_staff)
def admin_users_delete(request, pk):
    selected_user = Users.objects.get(id=pk) 
    #selected_user.delete() 
    # физическое удаление пользователя из БД. удаление через is_active сделаю позже, но сразу... до того как буду делать защиту через декоратор.
    if selected_user.is_active==True:
        selected_user.is_active=False 
    else:
        selected_user.is_active=True
    selected_user.save()
    return HttpResponseRedirect(reverse('admins:admin_users'))
  










#Категории товаров
class ProductCategoryListView(ListView): 
    model = ProductsCategory
    template_name = 'admins/admin-category-read.html' 
    
    # работа с контекстом
    def get_context_data(self, *,object_list=None, **kwargs):
        context = super().get_context_data() 
        context['title'] = 'GeekShop - категории CBV'     
        return context 
    
    # работа с декоратором
    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self,request, *args, **kwargs):
        return super().dispatch(request,*args, **kwargs)

# @user_passes_test(lambda u: u.is_staff)
# def admin_categorys(request):
    # context = {
        # 'title': 'GeekShop - категории',
        # 'categorys': ProductsCategory.objects.all(),
    # }
    # return render(request, 'admins/admin-category-read.html', context)

class ProductsCategoryCteateView(CreateView): 
    model = ProductsCategory
    template_name = 'admins/admin-category-create.html' 
    form_class = AdminsCategoryElementForm
    success_url = reverse_lazy('admins:admin_categorys')
    
    # работа с контекстом
    def get_context_data(self, *,object_list=None, **kwargs):
        context = super().get_context_data() 
        context['title'] = 'GeekShop - создание категории CBV'     
        return context 
    
    # работа с декоратором
    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self,request, *args, **kwargs):
        return super().dispatch(request,*args, **kwargs)

# @user_passes_test(lambda u: u.is_staff)
# def admin_categorys_create(request):
    # if request.method == 'POST':
        # form=AdminsCategoryElementForm(data=request.POST)
        # if form.is_valid():
            # form.save()
            # return HttpResponseRedirect(reverse('admins:admin_categorys'))
    # else:
        # form = AdminsCategoryElementForm()
    # context = {
        # 'title': 'GeekShop - категории',
        # 'form': form,
    # }
    # return render(request, 'admins/admin-category-create.html', context)

@user_passes_test(lambda u: u.is_staff)
def admin_categorys_update(request, key):
    selected_category = ProductsCategory.objects.get(id=key)
    if request.method == 'POST':
        form=AdminsCategoryElementForm(instance = selected_category, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_categorys'))
    else:
        form = AdminsCategoryElementForm(instance = selected_category)
    context = {
        'title': 'GeekShop - категории',
        'form': form,
        'selected_category': selected_category,
    }
    return render(request, 'admins/admin-category-update-delete.html', context)  

@user_passes_test(lambda u: u.is_staff)
def admin_categorys_delete(request, key):
    selected_category = ProductsCategory.objects.get(id=key)  
    selected_category.delete()
    return HttpResponseRedirect(reverse('admins:admin_categorys'))    










#Товары
class ProductsListView(ListView):
    model = Products
    template_name = 'admins/admin-products-read.html' 
    
    # работа с контекстом
    def get_context_data(self, *,object_list=None, **kwargs):
        context = super().get_context_data() 
        context['title'] = 'GeekShop - товары CBV'     
        return context 
    
    # работа с декоратором
    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self,request, *args, **kwargs):
        return super().dispatch(request,*args, **kwargs)


# @user_passes_test(lambda u: u.is_staff)
# def admin_products(request):
    # context = {
        # 'title': 'GeekShop - товары',
        # 'products': Products.objects.all(),
    # }
    # return render(request, 'admins/admin-products-read.html', context)

class ProductsCreateView(CreateView):
    model = Products
    template_name = 'admins/admin-products-create.html'
    form_class = AdminsProductElementForm
    success_url = reverse_lazy('admins:admin_products')
    
    # работа с контекстом
    def get_context_data(self, *,object_list=None, **kwargs):
        context = super().get_context_data() 
        context['title'] = 'GeekShop - новый товар CBV'     
        return context 
    
    # работа с декоратором
    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self,request, *args, **kwargs):
        return super().dispatch(request,*args, **kwargs)


# @user_passes_test(lambda u: u.is_staff)
# def admin_products_create(request):
    # if request.method == 'POST':
        # form=AdminsProductElementForm(data=request.POST, files = request.FILES)
        # if form.is_valid():
            # form.save()
            # return HttpResponseRedirect(reverse('admins:admin_products'))
    # else:
        # form = AdminsProductElementForm()
    # context = {
        # 'title': 'GeekShop - новый товар',
        # 'form': form,
    # }
    # return render(request, 'admins/admin-products-create.html', context)
    
@user_passes_test(lambda u: u.is_staff)
def admin_products_update(request, key):
    selected_product = Products.objects.get(id=key)
    if request.method == 'POST':
        form=AdminsProductElementForm(instance = selected_product, files = request.FILES, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_products'))
    else:
        form = AdminsProductElementForm(instance = selected_product)
    context = {
        'title': 'GeekShop - редактирование товара',
        'form': form,
        'selected_product': selected_product,
    }
    return render(request, 'admins/admin-products-update-delete.html', context)  

@user_passes_test(lambda u: u.is_staff)
def admin_products_delete(request, key):
    selected_product = Products.objects.get(id=key)  
    selected_product.delete()
    return HttpResponseRedirect(reverse('admins:admin_products'))    


