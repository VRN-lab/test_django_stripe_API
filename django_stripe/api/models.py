from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)


class Order(models.Model):
    items = models.ManyToManyField(Item)
