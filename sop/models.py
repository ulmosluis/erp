from django.db import models

# Create your models here.

from inv.models import Product
from pop.models import Supplier

class SaleDocument(models.Model):
    date = models.DateField()
    number = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    documentType = models.IntegerField(default=1)

    def __str__(self):
        return self.order_number

class SaleDocumentDetails(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(SaleDocument, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return f"{self.product} ({self.quantity})"

class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    contact_info = models.CharField(max_length=100)

    def __str__(self):
        return self.name
