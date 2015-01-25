from decimal import Decimal

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.mail import send_mail

import stripe

from orders.models import Order, Item
from payments.models import Payment

stripe.api_key = "sk_test_w96KeQLCTh23810DSE2ykwIt"


class BillingView(TemplateView):
    template_name = 'billing/index.html'

    def get_context_data(self, **kwargs):
        context = super(BillingView, self).get_context_data(**kwargs)
        context['price'] = self.request.session['price']
        return context

    def post(self, request, *args, **kwargs):
        token = request.POST.get("stripeToken")
        price = self.request.session['price']
        try:
            charge = stripe.Charge.create(
                # Stripe works in cents instead of dollars.
                # Multiply price by 100 to convert to cents
                amount = int(float(price)*100),

                currency="usd",
                card = token,
                description="For Donation"
            )
            order = Order.objects.create(email='james@gmail.com')
              
            payment = Payment.objects.create(order=order, total=Decimal(price))
            mssg = "You payed us " + str(payment.total)
            send_mail(
                'Order Information', 
                mssg,
                'support@benefica.org', 
                ['campusgino@gmail.com'], 
                fail_silently=False
            ) 
            return HttpResponse("You were succesfully charged $" + price)
        except stripe.CardError, e:
            return HttpResponse("its broken")  
