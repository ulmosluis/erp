
from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_description = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_code = models.CharField(max_length=100)
    product_description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.product_code






