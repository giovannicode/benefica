from decimal import Decimal

from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.mail import send_mail

import stripe

from orders.models import Order, Item
from payments.models import Payment
from products.models import Product

stripe.api_key = "sk_test_w96KeQLCTh23810DSE2ykwIt"


class BillingView(TemplateView):
    template_name = 'billing/index.html'

    def get_context_data(self, **kwargs):
        context = super(BillingView, self).get_context_data(**kwargs)
        total = 0 
        for product_id in self.request.session['cart']:
            total += Product.objects.get(pk=product_id).price
        context['price'] = str(total)
        self.request.session['total'] = str(total)
        return context

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        token = request.POST.get("stripeToken")
        total = self.request.session['total']
 
        payment = Payment.objects.create(total=Decimal(total)) 
        order = Order.objects.create(email='james@gmail.com', payment=payment)
        for product_id in self.request.session['cart']:
            product = Product.objects.get(pk=product_id)
            Item.objects.create(order=order, product=product, title=product.title, price=product.price)
                 
        try:
            charge = stripe.Charge.create(
                # Stripe works in cents instead of dollars.
                # Multiply price by 100 to convert to cents
                amount = int(float(total)*100),
                currency="usd",
                card = token,
                description="For Donation"
            )
            
            # If charge is successful this code will execute.  
            mssg = "Order ID: " + str(order.id) + "\n"
            mssg += "Total Charged: " + str(order.payment.total)

            send_mail(
                'Order Information', 
                mssg,
                'support@benefica.org', 
                ['campusgino@gmail.com'], 
                fail_silently=False
            ) 
            return HttpResponse("You were succesfully charged $" + total)
        except stripe.CardError, e:
            return HttpResponse("its broken")  
