"""test_project_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
import debug_toolbar
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('test_project_backend.apps.api.urls', namespace='api')),

    path('orders/', include('test_project_backend.apps.order.urls', namespace='order')),

    # DEVELOPMENT URLS - REMOVE AFTER PRODUCTION
    # path('admin/doc/', include('django.contrib.admindocs.urls')),
    # # debug toolbar url
    # path('__debug__/', include(debug_toolbar.urls)),
]
