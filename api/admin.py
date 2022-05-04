from django.contrib import admin

# Register your models here.
from api.models.product import Product
from api.models.user import User
from api.models.cart import Cart
from api.models.category import Category
from api.models.guidebook import Guidebook


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'products']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'rating', 'reviews', 'price', 'category']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'username', 'password']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Guidebook)
class GuidebookAdmin(admin.ModelAdmin):
    list_display = ['id', 'content']
