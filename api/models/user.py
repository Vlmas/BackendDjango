from django.db import models


class User(models.Model):
    name = models.TextField(default='')
    username = models.TextField(default='')
    password = models.TextField(default=0)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return f'{self.id}: {self.name}'
