from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    price = models.CharField(max_length=255)
    description = models.TextField()
    amount = models.IntegerField()
