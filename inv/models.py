from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name
    
class category(models.Model):
    categoryName = models.CharField(max_length=100)
    categoryDescription = models.CharField(max_length=200)

    def __str__(self):
        return self.categoryName
