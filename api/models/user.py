from django.db import models

from api.managers.user import UserManager
from api.models.cart import Cart


class User(models.Model):
    name = models.TextField(default='')
    username = models.TextField(default='')
    password = models.TextField(default='123')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE())

    objects = models.Manager()
    cart_related = UserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['username', 'name']

    def __str__(self):
        return f'{self.id}: {self.name}'
