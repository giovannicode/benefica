from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class PaymentView(TemplateView):
    template_name = 'payments/index.html'

    def post(self, request, *args, **kwargs):
        
    
