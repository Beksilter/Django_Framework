from django.contrib import admin

from products.models import Products, ProductsCategory;

@admin.register(Products)
class AdminProdicts(admin.ModelAdmin):
    list_display=('name','category', 'price','quantity')
    search_fields=('name',)
    fields = (('name', 'category'),'description', 'image', ('price', 'quantity'))

@admin.register(ProductsCategory)
class AdminProdicts(admin.ModelAdmin):
    list_display=('name','description')
    search_fields=('name',)
    
