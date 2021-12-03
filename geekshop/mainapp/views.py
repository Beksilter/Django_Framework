from django.shortcuts import render
from django.views.generic import DetailView

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

class ProductDetail(DetailView):
    """
    Контроллер вывода информации о продукте
    """
    model = Product
    template_name = 'mainapp/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        product = self.get_object()
        context['product'] = product
        return context