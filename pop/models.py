from django.db import models

# Create your models here.

    

class Supplier(models.Model):
    supplier_name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.supplier_name




