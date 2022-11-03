from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=32)
    product_slug = models.SlugField(max_length=32)
    product_description = models.TextField(null=True, blank=True)
    product_cost = models.PositiveIntegerField(default=0)
    availability = models.BooleanField(default=False)

