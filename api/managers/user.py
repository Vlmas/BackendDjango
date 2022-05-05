from django.db import models

from api.models.cart import Cart


class UserManager(models.Manager):
    def get_by_username(self, username):
        return self.filter(username=username)

    def get_by_name(self, name):
        return self.filter(name=name)

    def get_cart_by_user_id(self, user_id):
        return self.filter()

