from rest_framework import serializers

from ..models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'amount', 'amount_currency', 'comment', 'is_payed', 'order_id', 'created_at', 'updated_at',)
        model = Order
