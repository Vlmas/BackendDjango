from django.db import models
from django.contrib.postgres.fields import ArrayField


class Guidebook(models.Model):
    content = ArrayField(models.TextField(default=''))

    class Meta:
        verbose_name = 'Guidebook'
        verbose_name_plural = 'Guidebooks'

    def __str__(self):
        return f'{self.id}: Guidebook'
