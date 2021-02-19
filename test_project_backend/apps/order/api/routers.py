from test_project_backend.apps.order.api import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("orders", views.OrderViewSet, "orders")
