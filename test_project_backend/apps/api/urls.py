from django.urls import include, path

# from .routers import router

app_name = 'api'
urlpatterns = [
    # path('', include(router.urls), ),
    path('', include('test_project_backend.apps.order.api.urls', )),
]
