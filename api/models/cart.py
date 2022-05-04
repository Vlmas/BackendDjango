from django.db import models
from api.models.product import Product


class Cart(models.Model):
    products = models.ManyToManyField(Product, blank=True)

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

    def __str__(self):
        return f'{self.id}: Cart'
