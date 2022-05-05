from django.db import models
from api.managers.product import ProductManager
from api.models.category import Category


class Product(models.Model):
    name = models.TextField(default='')
    description = models.TextField(default='')
    rating = models.FloatField(default=0)
    reviews = models.IntegerField(default=0)
    price = models.FloatField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    category_related = ProductManager()
    objects = models.Manager()

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['name', 'rating', 'price']

    def __str__(self):
        return f'{self.id}: {self.name}, {self.category}'