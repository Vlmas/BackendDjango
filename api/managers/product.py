from django.db import models

from api.models.category import Category


class ProductManager(models.Manager):
    def get_by_category(self, category):
        return self.filter(category=category)

    def get_by_description(self, description):
        return self.filter(description=description)

    def get_by_better_rating(self, rating):
        return self.filter(rating=rating)

    def get_by_better_reviews(self, reviews):
        return self.filter(reviews=reviews)

    def get_products_by_category(self, category_name):
        category = Category.objects.get(name=category_name)
        return self.filter(category_id=category.id)
