from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View

import stripe

from .models import Item, Order
from django_stripe.settings import SECRET_KEY_STRIPE


stripe.api_key = SECRET_KEY_STRIPE


class BuyView(View):
    """
    Класс представления, который осществляет
    обработку покупки через Stripe
    """
    def get(self, request, *args, **kwargs):
        item = get_object_or_404(Item, id=kwargs['id'])
        success_url = self.request.build_absolute_uri(
            reverse_lazy('api:success')
        )
        cancel_url = self.request.build_absolute_uri(
            reverse_lazy('api:cancel')
        )
        session = self.create_stripe_session(
            item, success_url, cancel_url
        )
        return JsonResponse({'session_id': session.id})

    def create_stripe_session(self, item, success_url, cancel_url):
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount': int(item.price * 100),
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=success_url,
            cancel_url=cancel_url,
        )

        return session


class ItemView(View):
    """
    Класс представления, показывает товар если он есть
    """
    def get(self, request, *args, **kwargs):
        item = get_object_or_404(Item, id=kwargs['id'])
        return render(request, 'item.html', {'item': item})


class ItemsView(View):
    """
    Класс представления, показывает группу товаров если они есть
    """
    def get(self, request, *args, **kwargs):
        items = Item.objects.all()
        return render(request, 'items.html', {'items': items})


class SuccessView(View):
    """
    Класс представления, показывает страницу успешной покупки
    """
    def get(self, request, *args, **kwargs):
        return render(request, 'success.html')


class CancelView(View):
    """
    Класс представления, отмены покупки
    """
    def get(self, request, *args, **kwargs):
        return render(request, 'cancel.html')


@method_decorator(csrf_exempt, name='dispatch')
class CreateOrderView(View):
    """
    Класс представления, брабатывает создание заказа и оплату через Stripe
    """
    def post(self, request, *args, **kwargs):
        item_ids = request.POST.getlist('items')
        items = Item.objects.filter(id__in=item_ids)
        order = Order.objects.create()
        success_url = request.build_absolute_uri(reverse_lazy('api:success'))
        cancel_url = request.build_absolute_uri(reverse_lazy('api:cancel'))
        order.items.set(items)
        order.save()

        total_amount = sum(item.price for item in items)

        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': 'Order #' + str(order.id),
                    },
                    'unit_amount': int(total_amount * 100),
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=success_url,
            cancel_url=cancel_url,
        )

        return JsonResponse({'session_id': session.id})
