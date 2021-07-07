from django.db import models
from django.db.models.base import Model


class Widget(models.Model):
    description = models.CharField(max_length=20)
    quantity = models.IntegerField()

    def __str__(self):
        return self.description