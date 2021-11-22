from django.shortcuts import render

import os

MODULE_DIR=os.path.dirname(__file__)
# Create your views here.

def index(request):
    context = {
        'title': 'Geekshop', }
    return render(request, 'mainapp/index.html', context)

def products(request):
    from mainapp.models import Product, ProductCategory
    context = {
        'title': 'GeekShop - Каталог',
        'products': Product.objects.all(),
        'category':ProductCategory.objects.all(),
    }

    return render(request, 'mainapp/products.html', context)
