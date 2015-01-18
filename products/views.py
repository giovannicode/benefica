from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from django.contrib.auth.decorators import login_required

from products.models import Product
from customusers.models import User

# Create your views here.
@login_required(redirect_field_name=None)
def add(request):
    if request.method == 'GET':
	form = ProductForm 
	return render(request, 'products/add.html', {'form': form})
    
    elif request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.user = User.objects.get(pk=request.user.id)
            product.save()
            return redirect('main:index') 
        else:
            return render(request, 'products/add.html', {'form': form})

class ProductCreateView(CreateView):
    model = Product
    fields = ['title', 'description', 'image', 'price']

    def form_valid(self, form):
        product = form.save(commit=False)
        product.user = User.objects.get(pk=self.request.user.id) 
        product = form.save()
        return redirect('profiles:index')

class ProductListView(ListView):  
    model = Product            
    template_name = 'main/index.html'
