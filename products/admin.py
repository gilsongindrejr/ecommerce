from django.contrib import admin

from .models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ('category',)
    ordering = ('category',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('name', 'price', 'stock', 'category', 'slug')
    list_filter = ('category',)
    ordering = ('name',)

