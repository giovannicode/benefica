from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

import stripe


stripe.api_key = "sk_test_w96KeQLCTh23810DSE2ykwIt"


class PaymentView(TemplateView):
    template_name = 'payments/index.html'

    def post(self, request, *args, **kwargs):
        token = request.POST.get("stripeToken")
        price = self.request.session['price']
        price = int(price)
        try:
            charge = stripe.Charge.create(
                amount = price,
                currency="usd",
                card = token,
                description="For Donation"
            )
            return HttpResponse("You were succesfully charged " + str(price))
        except stripe.CardError, e:
            return HttpResponse("its broken")
