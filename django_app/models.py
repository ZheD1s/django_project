from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    description = models.TextField(null=False, blank=False)
    price = models.PositiveIntegerField(null=False, blank=False)
    manufacturing_date = models.DateTimeField(null=False, blank=False)

    def __str__(self):
        return str(self.name)

class Manufacturer(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    capital = models.PositiveBigIntegerField(null=False, blank=False)
    country = models.CharField(max_length=100, null=False, blank=False, unique=True)
    president = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return str(self.name)

class Fruit(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    description = models.TextField(null=False, blank=False)
    price = models.PositiveIntegerField(null=False, blank=False)
    manufacturing_date = models.DateTimeField(null=False, blank=False)

    def __str__(self):
        return str(self.name)