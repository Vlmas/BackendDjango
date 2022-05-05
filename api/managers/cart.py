from django.db import models


class CartManager(models.Manager):
    def get_by_product(self, product):
        return self.filter(product=product)
