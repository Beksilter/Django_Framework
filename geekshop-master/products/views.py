from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 
        # последние двое - это исключения пагинатора

def index(request):
    context = {
        'title': 'Интернет-магазин GeekShop (учебный проект на Django)',
    }
    return render(request, 'products/index.html', context)


def products(request, category_id=None, page=1):
    import datetime
    from products.models import Products, ProductsCategory
    
    if category_id:
        products_filter = Products.objects.filter(category_id=category_id) 
            # фильтруем по идентификатору внутри справочника категорий 
            # по значению category_id, которое пришло из переменных вызова функции.
    else:
        products_filter = Products.objects.all()    
    paginator = Paginator(products_filter, 6) # где число - это количесвто товаров на странице
        # создали пагинатор
    try:
        products_paginator = paginator.page(page)
            # получили список товаров на странице page
    except PageNotInteger:
        products_paginator = paginator.page(1)
                # отобразим первую страницу
    except EmptyPage:
        products_paginator = paginator.page(pagintor.num_pages())
                # отобразим вообще все товары
    context = {
            'title': 'GeekShop - каталог наших предложений',
            'date': datetime.datetime.now().today(),
            'products': products_paginator,  # Заменили фильтр на пагинатор
            'category': ProductsCategory.objects.all()
        }
    return render(request, 'products/products.html', context)
