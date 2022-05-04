from django.db import models
from api.models.category import Category


class Product(models.Model):
    name = models.TextField(default='')
    description = models.TextField(default='')
    rating = models.FloatField(default=0)
    reviews = models.IntegerField(default=0)
    price = models.FloatField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['name']

    def __str__(self):
        return f'{self.id}: {self.name}, {self.category}'
