from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=32)
    category_slug = models.SlugField(max_length=32)
    category_description = models.TextField(null=True, blank=True)