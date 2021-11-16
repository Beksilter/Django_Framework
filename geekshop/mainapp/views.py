from django.shortcuts import render


# Create your views here.

def index(request):
    context = {
        'title': 'Geekshop', }
    return render(request, 'mainapp/index.html', context)


# def products(request):
#     context = {'title': 'GeekShop - Каталог',
#                'products': [{'name': 'Худи черного цвета с монограммами adidas Originals',
#                              'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
#                              'price': '6 090,00', 'image': '/static/vendor/img/products/Adidas-hoodie.png'},
#                             {'name': 'Синяя куртка The North Face',
#                              'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
#                              'price': '23 725,00', 'image': '/static/vendor/img/products/Blue-jacket-The-North-Face.png'},
#                             {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
#                              'description': 'Материал с плюшевой текстурой. Удобный и мягкий.', 'price': '3 390,00',
#                              'image': '/static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png'},
#                             {'name': 'Черный рюкзак Nike Heritage спортивный oversized-топ ASOS DESIGN',
#                              'description': 'Плотная ткань. Легкий материал.', 'price': '2 340,00',
#                              'image': '/static/vendor/img/products/Black-Nike-Heritage-backpack.png'},
#
#                             {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
#                              'description': 'Гладкий кожаный верх. Натуральный материал.', 'price': '13 590,00',
#                              'image': '/static/vendor/img/products/Black-Dr-Martens-shoes.png'},
#
#                             {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
#                              'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.', 'price': '2 890,00',
#                              'image': '/static/vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png'}]}
#
#     return render(request, 'mainapp/products.html', context=context)


def products(request):
    import json
    with open('mainapp/fixtures/products.json',encoding='utf-8') as f:
        products = json.load(f)
    context = {'title': 'GeekShop - Каталог',
               'products': products
               }
    return render(request, 'mainapp/products.html', context)
