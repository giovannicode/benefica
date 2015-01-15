from django.shortcuts import render
from products.models import Product

# Create your views here.
def index(request):
    products = Product.objects.all() 
    return render(request, 'main/index.html', {'products':products})
