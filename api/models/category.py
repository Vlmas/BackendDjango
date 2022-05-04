from django.db import models


class Category(models.Model):
    name = models.TextField(default='')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return f'{self.id}: {self.name}'
