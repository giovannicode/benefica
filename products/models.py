from django.conf import settings
from django.db import models
from django.forms import ModelForm


class Product(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products')
    price = models.DecimalField(max_digits=14, decimal_places=2)
    qty = models.PositiveIntegerField()
