from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from test_project_backend import settings
from ..api.serializers import OrderSerializer

from ..models import Order


class OrderViewSetTest(APITestCase):
    """
    Test Order view set
    """
    fixtures = ['auth', 'order', ]

    @classmethod
    def setUpClass(cls):
        super(OrderViewSetTest, cls).setUpClass()
        cls.url = reverse('api:orders-list')

    def test_get_orders_api_payed_list(self):
        """Test get payed orders api list"""
        response = self.client.get(self.url)

        orders = Order.objects.filter(is_payed=True)

        orders_ser = OrderSerializer(orders, many=True)

        self.assertEqual(response.data, orders_ser.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_orders_payed_and_un_payed(self):
        """Test get all orders payed and un payed"""
        response = self.client.get(self.url, data={'get_all': True})

        orders = Order.objects.all()

        orders_ser = OrderSerializer(orders, many=True)

        self.assertEqual(response.data, orders_ser.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_order_api(self):
        """Test create order"""
        data = {
            "amount": '10',
            "comment": "Comment test"
        }
        response = self.client.post(self.url, data, format='json')

        print(f'Response data test order create: {response.data}')


class OrderRegisterDoAPIView(APITestCase):
    fixtures = ['auth', 'order', ]

    @classmethod
    def setUpClass(cls):
        super(OrderRegisterDoAPIView, cls).setUpClass()
        cls.url = reverse('api:order-register')

    def test_post_method(self):
        order = Order.objects.filter(is_payed=True)[0]
        data = {
            'userName': settings.SHOP_LOGIN,
            'password': settings.SHOP_PASSWORD,
            'orderNumber': order.pk,
            'amount': order.amount.amount,
            'currency': order.amount.currency.numeric,
            'returnUrl': f'orders/{order.pk}'
        }

        response = self.client.post(self.url, data, format='json')
        print(f'Test case response: {response.data}')
