from django.conf import settings
from django.db import models
from django.forms import ModelForm

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products')
    price = models.DecimalField(max_digits=14, decimal_places=2)

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'image', 'price']
