import uuid
from decimal import Decimal

from django.db import models
from django.utils.translation import gettext_lazy as _

from djmoney.models.fields import MoneyField
# from djmoney.models.validators import MinMoneyValidator

from test_project_backend.apps.core.models import CreationModificationDateBase


class Order(CreationModificationDateBase):
    """Order model"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=_('ID'))
    amount = MoneyField(max_digits=14,
                        decimal_places=2,
                        default_currency='TMT',
                        verbose_name=_('Amount'),
                        # validators=[MinMoneyValidator(Decimal('1.0'))]
                        )
    comment = models.TextField(max_length=500, verbose_name=_('Comment'))
    is_payed = models.BooleanField(default=False, verbose_name=_("Is payed"))
    order_id = models.UUIDField(null=True, blank=True)
