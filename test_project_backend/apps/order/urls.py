from django.urls import path
from .views import SuccessOrderView, FailOrderView


app_name = 'order'
urlpatterns = [
    path('success/', SuccessOrderView.as_view(), name='order-success'),
    path('fail/', FailOrderView.as_view(), name='order-fail'),
]
