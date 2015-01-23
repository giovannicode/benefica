from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from products.models import Product
# Create your views here.
class CartView(TemplateView):
    template_name = 'carts/index.html'
     
    def post(self, request, *args, **kwargs):
        product = Product.objects.get(pk=request.POST.get("product_id"))
        request.session['price'] = str(product.price)
        return HttpResponse('')
