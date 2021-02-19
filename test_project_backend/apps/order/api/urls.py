from django.urls import include, path

from .routers import router
from .views import OrderRequestDoAPIView

urlpatterns = [
    path('', include(router.urls)),
    path('order_register/', OrderRequestDoAPIView.as_view(), name='order-register')
]
