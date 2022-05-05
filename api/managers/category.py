from django.db import models


class CategoryManager(models.Manager):
    def get_by_name(self, name):
        return self.filter(name=name)

    def get_products(self):
        pass
