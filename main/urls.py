"""main URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # user
    path('api/users/', include('user_models.urls')),
    # Customer Api
    path('api/customers/', include('pcr_models.customers.customers.urls')),
    # Staff Api
    path('api/staffs/', include('pcr_models.staffs.staffs.urls')),
    path('api/staff-groups/', include('pcr_models.staffs.staff_groups.urls')),
    # Product Api
    path('api/products/', include('pcr_models.products.products.urls')),
    path('api/product-builds/', include('pcr_models.products.product_builds.urls')),
    path('api/product-supplies/', include('pcr_models.products.product_supplies.urls')),
    path('api/product-stocks/', include('pcr_models.products.product_stocks.urls')),
    # Supplier
    path('api/suppliers/', include('pcr_models.suppliers.suppliers.urls')),
    # Order Api
    path('api/orders/', include('pcr_models.orders.orders.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
