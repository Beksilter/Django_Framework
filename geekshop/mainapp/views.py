from django.shortcuts import render
from mainapp.models import Product, ProductCategory
import os

MODULE_DIR=os.path.dirname(__file__)
# Create your views here.

def index(request):
    context = {
        'title': 'Geekshop', }
    return render(request, 'mainapp/index.html', context)

def products(request):
    context = {
        'title': 'GeekShop | Каталог',
        'products': Product.objects.all(),
        'categories':ProductCategory.objects.all(),
    }

    return render(request, 'mainapp/products.html', context)
