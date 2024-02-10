from django.db import models

# Create your models here.

class Product(models.Model):
    productName = models.CharField(max_length=100)
    productDescription = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name
    
class category(models.Model):
    categoryName = models.CharField(max_length=100)
    categoryDescription = models.CharField(max_length=200)

    def __str__(self):
        return self.categoryName

class Warehouse(models.Model):
    warehouseName = models.CharField(max_length=100)
    warehouseAddress = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=100)

    def __str__(self):
        return self.warehouseName