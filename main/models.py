from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    description = models.TextField()
    amount = models.IntegerField()
