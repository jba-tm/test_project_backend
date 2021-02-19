import requests as r_requests
from django.views.generic import RedirectView

from test_project_backend import settings
from test_project_backend.apps.order.models import Order


class SuccessOrderView(RedirectView):
    url = settings.ORDER_REDIRECT_RETURN_URL

    def get(self, request, *args, **kwargs):
        order_id = request.GET.get('orderId', None)
        data = {
            'userName': settings.SHOP_LOGIN,
            'password': settings.SHOP_PASSWORD,
            'orderId': order_id
        }

        r = r_requests.post(settings.ORDER_STATUS_CHECK_URL, json=data)
        r_data = r.json()
        if r_data['orderStatus'] == 2:
            try:
                order = Order.objects.get(order_id=order_id)
                order.is_payed = True
                order.save()
                self.url = f"{settings.ORDER_REDIRECT_RETURN_URL}?" \
                           f"orderStatus={r_data['orderStatus']}&message={r_data['errorMessage']}"
            except Order.DoesNotExist:
                pass

        return super().get(request, data=r_data, *args, **kwargs)


class FailOrderView(RedirectView):
    url = f'{settings.ORDER_REDIRECT_RETURN_URL}?message="Your order canceled"'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
