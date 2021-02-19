from decimal import Decimal

from rest_framework.reverse import reverse_lazy
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.views import APIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework import status

from moneyed import get_currency
import requests as http_requests

from test_project_backend import settings
from ..models import Order
from .serializers import OrderSerializer


class OrderViewSet(CreateModelMixin, ReadOnlyModelViewSet):
    queryset = Order.objects.filter(is_payed=True)
    serializer_class = OrderSerializer
    order_register_do_url = settings.ORDER_REGISTER_URL
    order_success_url = reverse_lazy('order:order-success')
    order_fail_url = reverse_lazy('order:order-fail')

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        # headers = self.get_success_headers(serializer.data)
        order = Order.objects.get(pk=serializer.data['id'])

        data = {
            "language": "tk",
            "pageView": "checkout",
            "description": "Description",
            "failUrl": f'{settings.BASE_URL}{self.order_fail_url}',
            'userName': settings.SHOP_LOGIN,
            'password': settings.SHOP_PASSWORD,
            'orderNumber': str(order.pk),
            'amount': int(Decimal(order.amount.amount) * 100),
            'currency': order.amount.currency.numeric,
            'returnUrl': f'{settings.BASE_URL}{self.order_success_url}'
        }

        r = http_requests.post(self.order_register_do_url, json=data)
        r_data = r.json()
        order.order_id = r_data['orderId']
        order.save()

        return Response(data=r_data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        get_all = self.request.query_params.get('get_all', None)
        if get_all:
            return Order.objects.all()
        else:
            return super().get_queryset()


class OrderRequestDoAPIView(APIView):
    def get(self, request, format=None):
        response_data = {
            'orderId': request.data.get('orderNumber'),
            'formUrl': f'/checkout/{request.data.get("orderNumber")}',
            'errorCode': 0,
            'errorMessage': None
        }
        return Response(data=response_data, status=status.HTTP_200_OK)
