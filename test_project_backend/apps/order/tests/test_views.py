from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from test_project_backend.apps.order.models import Order


class SuccessOrderViewTest(TestCase):
    fixtures = ['auth', 'order']

    @classmethod
    def setUpClass(cls):
        super(SuccessOrderViewTest, cls).setUpClass()
        cls.url = reverse('order:order-success')

    def test_view_with_get_method(self):
        order = Order.objects.filter(order_id__isnull=False).last()

        data = {
            'orderId': order.order_id,
            # 'userName': settings.SHOP_LOGIN,
            # 'password': settings.SHOP_PASSWORD,
        }

        response = self.client.get(self.url, data)
        order_after = Order.objects.get(pk=order.pk)
        self.assertTrue(order_after.is_payed)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        print(response)
