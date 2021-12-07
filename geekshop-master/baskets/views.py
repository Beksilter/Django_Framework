from django.shortcuts import render, HttpResponseRedirect
from products.models import Products
from baskets.models import Basket
from django.contrib.auth.decorators import login_required

# для работы ajax
from django.template.loader import render_to_string
from django.http import JsonResponse

@login_required
def basket_add(request, product_id):
    product = Products.objects.get(id=product_id) # взяли нужный продукт (с которого на кнопку нажали)
    baskets = Basket.objects.filter(user = request.user, product=product) 
    # отфильтровали корзину по нужному продукту и пользователю
    # если есть - то нужно +=1, если нет, то нужно создать 1
    if not baskets.exists():
        Basket.objects.create(user = request.user, product = product, quantity = 1) # создали запись в корзине на 1 единицу товара
        return HttpResponseRedirect(request.META.get('HTTP_REFERER')) # вернулись туда откуда пришли
    else:    
        basket = baskets.first() # взяли любой, потому что первый - он и последний.
        basket.quantity+=1 # +=1..
        basket.save() # сохранили изменение количества
        return HttpResponseRedirect(request.META.get('HTTP_REFERER')) # вернулись туда откуда пришли

@login_required
def basket_remove(request, id): #здесь id это id корзины а не товара.
    basket = Basket.objects.get(id=id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
@login_required
def basket_edit(request, id, quantity):
    """
    тут в контроллер передается собственно запрос, который содержит общие данные, идентификатор корзины которую нужно изменить, новое актуальное количество, которое нужно записать в корзину. а сумма считается при выводе через контроллер или ч/з модель (у меня модель)
    """
    if request.is_ajax():                       # запрос пришел от ajax
        basket = Basket.objects.get(id=id)      # выбрали корзину с нужным id
        if quantity>0:                          # если актуальное количесвто > 0 - перепишем корзину
            basket.quantity = quantity
            basket.save()
        else:                                   # если 0 или меньше - удалим корзину
            basket.delete()
        # корзина изменена, теперь ее нужно «показать», возвратив ответ.
        # дял этого делаем то-же что и в контроллере, но дял «кусочка» страницы, которую нужно обновить.
        baskets = Basket.objects.filter(user = request.user)            # берем все корзины пользователя
        context = {'baskets': baskets}                                  # формируем контекст
        result = render_to_string('baskets/basket.html', context)       # рендерим
        return JsonResponse({'result': result})                         # возвращаем рез-т
            
