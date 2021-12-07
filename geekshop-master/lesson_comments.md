# Комментарии к домашнему заданию текущего урока 

### 1. Организовать фильтрацию продуктов по категориям.
Для того, чтобы это сделать нужно изменить контроллер, шаблон и пространство адресов.
контроллер примет вид:
```python
def products(request, category_id=None):
    import datetime
    from products.models import Products, ProductsCategory
    
    if category_id:
        products_filter = Products.objects.filter(category_id=category_id) # фильтруем по идентификатору внутри справочника категорий по значению category_id, которое пришло из переменных вызова функции.
    else:
        products_filter = Products.objects.all()    
    
    context = {
            'title': 'GeekShop - каталог наших предложений',
            'date': datetime.datetime.now().today(),
            'products': products_filter,
            'category': ProductsCategory.objects.all()
        }
    return render(request, 'products/products.html', context)
```
пространство адресов:
```python
urlpatterns = [
    path('',products, name = 'index'), # но это уже index не от сайта а от пространства адресов products
    path('<int:category_id>',products, name = 'category') # адрес будет ../category/<id>
]
```
а часть шаблона, отвечающая за показ перечня категорий :
```html
{%for cat in category%}
<div class="list-group">
    <a href="{% url 'products:category' cat.id %}" class="list-group-item">{{cat.name}}</a>
</div>
{%endfor%}
```
проверил, закоммитил.

### 2. Организовать постраничный вывод в каталоге (пагинацию).
В джанго встроен класс пагинации, который называется pagination, если поуглить то можно получить исчерпывающий ответ на тему того что он делает и какие у него методы.
В связи с его применением код изменится следующим образом:
контроллер
```python
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
```
пространство адресов для products
```python
urlpatterns = [
    path('',products, name = 'index'), # но это уже index не от сайта а от пространства адресов products
    path('<int:category_id>/',products, name = 'category'), # адрес будет ../category/<id> 
    path('page/<int:page>/',products, name = 'page'), 
]
```
часть шаблона products которая отвечает за пагинатор
```html
<nav aria-label="Page navigation example">
    <ul class="pagination justify-content-center">
        <li class="page-item {% if not products.has_previous %} disabled {%endif%}">
            <a class="page-link" 
                href="{% if products.has_previous%} {% url 'products:page' products.previous_page_number%} {% else %} # {%endif%}" 
                tabindex="-1" aria-disabled="true">
                Предыдущая
            </a>
        </li>
        {% for page in products.paginator.page_range %}
            <li class="page-item">
                <a class="page-link" href="{% url 'products:page' page %}">
                    {{page}}
                </a>
            
            </li>
        {%endfor%}
        <li class="page-item {% if not products.has_next %} disabled {%endif%}">
            <a class="page-link" 
                href="{% if products.has_next%} {% url 'products:page' products.next_page_number%} 
                {% else %} # {%endif%}">
                Следующая</a>
        </li>
    </ul>
</nav>
```

### 3. Перевести как можно больше контроллеров в проекте на CBV.

Эту часть домашнего задания довел до подключения двух видов контроллеров - на создание и на чтение (без изменения данных). Поскольку задание обязательное, а я его не выполнил - то сдавать его не буду, и как результат не получу свои 10 последних баллов ((( . В любом случае, я знаю что большую часть курса прошол и сделал это хорошо.

Осталось разбираться во многих вещах, но я так мыслю что теперь это сделать станет гораздо проще. Поскольку дальнейшая учеба на этом курсе у меня, скорее всего, не получится, то думаю что достаточно многого достиг. 

Дальше этот проект будет развиваться, но уже в другой плоскости + я на его основе стану изучать джанго самостоятельно.

Подробно о том, что есть CBV в конце обобщающего докуентального файла.

