from django.db import models
from django import forms


class PaymentForm(forms.Form):
    first_name = forms.CharField(label='First Name')
  
    class Meta:
        abstract = True


class Payment(models.Model):
    total = models.DecimalField(max_digits=14, decimal_places=2)
