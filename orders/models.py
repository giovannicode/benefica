from django.db import models
from django.conf import settings

from products.models import Product

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    

class Item(models.Model):
    order = models.ForeignKey(Order)
    product = models.ForeignKey(Product)

