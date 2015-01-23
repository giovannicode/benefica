from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

import stripe


stripe.api_key = "sk_test_w96KeQLCTh23810DSE2ykwIt"


class PaymentView(TemplateView):
    template_name = 'payments/index.html'
   
    def get_context_data(self, **kwargs):
        context = super(PaymentView, self).get_context_data(**kwargs)
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
            return HttpResponse("You were succesfully charged $" + price)
        except stripe.CardError, e:
            return HttpResponse("its broken")
