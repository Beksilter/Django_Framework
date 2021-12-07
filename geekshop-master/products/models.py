from django.db import models

'''
тут
unque - уникальный
blank - флаг пустого значения (для стрингов "")
null - флаг значения nothing (none, null)
upload_to - название папки када загружать картинки
'''
'''
Поскольку подключены картинки (которые нужно загружать)
может понадобиться установить пакет pillow.
его можно поставить прамо в окружение через терминал командой pip.
Сообщение о необходимости такой установки выскочит при запуке сервера.
'''

class ProductsCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True,null=True, default='')
    # у нас картинка может быть пустой, поэтому нужно предусмотреть хренение специального изображения,
    # котороя будет отображаться для таких товаров и прописать его константой во вьювах (ну например blank_img).
    image = models.ImageField(blank=True, upload_to='products_img')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    # чисто теоретически хранить склад прямо в таблице товаров неправильно,
    # но с практической точки зрения и при небольшом обороте может быть даже удобно
    # PositiveIntegerField - неотрицательное целое значение. Опять же если товары предполагают граммы
    # - то нужен гругой тип... или стандартные учетные единицы дял поставки в штуках.
    quantity = models.PositiveIntegerField(default=0)
    # теперь подкючение таблицы по ключу
    category = models.ForeignKey(ProductsCategory, on_delete=models.CASCADE)
    # тут предусмотрено каскадное удаление записей в таблице товаров при удалении их категории.
    # Это очень неправильно, но в учебных целях пойдет. На нормальном проекте лучше поставить
    # models.SET_NULL тогда при удалении категории у соответсвующих товаров это поле будет обнуляться.
    # или models.PROTECT - тогда удалить категорию будет не возможно, если к ней отнесен хоть один товар.
    
    def __str__(self):
        return f'{self.name} | {self.category.name}'
