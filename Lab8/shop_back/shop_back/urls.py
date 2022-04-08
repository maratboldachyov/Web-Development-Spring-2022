"""shop_back URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from api.views import Products_List, Categories_List, Product_Details, Category_Details, Sorted_Products

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/products/', Products_List),
    path('api/products/<int:product_id>/', Product_Details),
    path('api/categories/', Categories_List),
    path('api/categories/<int:category_id>/', Category_Details),
    path('api/categories/<int:category_id>/products/', Sorted_Products),
]
