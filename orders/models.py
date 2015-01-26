from django.db import models
from django.conf import settings

from products.models import Product
from payments.models import Payment

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    email = models.EmailField()
    payment = models.OneToOneField(Payment)

    def __unicode__(self):
        str_items = ""
        for item in self.item_set.all():
            str_items += str(item) 
        return "\n" + self.email + "Payment Total: " + str(self.payment.total) + "\n   items:" + str_items   


class Item(models.Model):
    order = models.ForeignKey(Order)
    product = models.ForeignKey(Product)
    title = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=14, decimal_places=2)

    def __unicode__(self):
        return "\n   item: " + self.title + ", Price: " + str(self.price)



