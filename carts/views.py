import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from products.models import Product
# Create your views here.
class CartView(TemplateView):
    template_name = 'carts/index.html'
     
    def post(self, request, *args, **kwargs):
        request.session['cart'].append(request.POST.get("product_id"))
        request.session.modified = True
        return HttpResponse(json.dumps(request.session['cart']))
