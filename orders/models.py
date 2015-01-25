from django.db import models
from django.conf import settings

from products.models import Product

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    email = models.EmailField()
    

class Item(models.Model):
    order = models.ForeignKey(Order)
    product = models.ForeignKey(Product)
    tile = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=14, decimal_places=2)



