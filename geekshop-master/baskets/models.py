from django.db import models
from django.db.models import Sum
from users.models import Users
from products.models import Products

# Create your models here.

class Basket(models.Model):
    user = models.ForeignKey(Users, on_delete = models.CASCADE)
    product = models.ForeignKey(Products, on_delete = models.CASCADE)
    quantity= models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add = True) # Это
    # нужно для того чтобы в любой момент можно было поднять историю
    # о том, когда пользователь добавил товар в корзину.
    # а дял того, чтобы можно было проверять когда он ее изменял -
    # аналогичным образом можно создать modify_timestamp и при каждом
    # изменении это значение пререписывать.

    def __str__(self):
        return f'корзина для {self.user.username}| Товар {self.product.name}'
    
    def sum(self): 
        # здесь сделать метод в который будет что-то передаваться не 
        # получится. Его тогда невозможно будет вызвать из html
        # в этом случае нужные данные считаются в контроллере
        return self.quantity*self.product.price

    '''
    вызвать данные в шаблоне можно обратившись к ним как baskets.0.<имя_метода>
    костыль конечно - но более менее работает... чтото более умное в голову не пришло. 
    да и этот вариант до конца не реализовал. 
    

    #Почему-то кажется, что не в ту сторону вообще 
    # ковыряю. задание со звездочкой и оно решается через контроллер в 
    # принципе достаточно адекватно и фильтрация там работает на «5»
    
    @classmethod
    def total_quantity(cls): # cls вместо self чтобы не путаться
        res  = cls.objects.all().aggregate(Sum('quantity')) 
        return res['quantity__sum']        
    
    @classmethod
    def total_sum(cls):
        data = cls.objects.all() # пробовал тут использовать filter, но не пошло.
        res=0
        for i in data:
            res+=i.sum()
        return res
    
    оказалось что думал правильно, и вызывал в шаблоне - тоже... просто несколько неверно подошол к вопросу перебора в итерации
    нужно было несколько по-другому делать фильтрацию
    '''
    
    @property
    def baskets(self):
        return Basket.objects.filter(user=self.user)
            
    def total_quantity(self):
        return sum(basket.quantity for basket in self.baskets)  # baskets, который property    
    
    def total_sum(self):
        return sum(basket.sum() for basket in self.baskets) # baskets, который property    
