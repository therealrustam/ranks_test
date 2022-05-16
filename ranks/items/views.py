import stripe
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView

from .models import Item


stripe.api_key = 'sk_test_51L05XxHjkc2r11YwYZk3iEjtVLNbob59E9LmkF88AQK8hYjprMpyrxacFNQD9egaorcVoaQBidOnS8r2sEy5M5aq00WtYPgJaQ'


def buy_item(request, buy_id):
    item = get_object_or_404(Item, id=buy_id)
    checkout_session = stripe.checkout.Session.create(
        success_url='http://127.0.0.1:8000/success/',
        cancel_url='http://127.0.0.1:8000/cancelled/',
        payment_method_types=['card'],
        mode='payment',
        line_items=[
            {
                'name': item.name,
                'quantity': 1,
                'currency': 'usd',
                'amount': item.price,
            }
        ]
    )
    return JsonResponse({'id': checkout_session['id']})


def get_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    context = {
        'item': item,
    }
    return render(request, 'home.html', context)


class SuccessView(TemplateView):
    template_name = 'success.html'


class CancelledView(TemplateView):
    template_name = 'cancelled.html'
