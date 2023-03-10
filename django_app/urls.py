from django.urls import path, include
from django.views.generic.base import TemplateView
from .views import *


urlpatterns = [
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('fruits/all/', FruitListView.as_view(), name='fruits'),
    path('fruits/<int:pk>/', FruitDetailView.as_view(), name='fruit_detail'),
    path('fruit/new/', FruitCreateView.as_view(), name='fruit_create'),
    path('fruit/<int:pk>/update/', FruitUpdateView.as_view(), name='fruit_update'),
    path('fruit/<int:pk>/delete', FruitDeleteView.as_view(), name='fruit_delete'),
    path('product/new/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('manufacturers/', ManufacturersListView.as_view(), name='manufacturers'),
    path('manufacturers/<int:pk>/', ManufacturersDetailView.as_view(), name='manufacturer_detail'),
    path('manufacturers/new/', ManufacturersCreateView.as_view(), name='manufacturer_create'),
    path('manufacturers/<int:pk>/update', ManufacturersUpdateView.as_view(), name='manufacturer_update'),
    path('', ProductListView.as_view(), name='home'),
]

# path(<url:str>, <view:<class:view>>, name=<name:str>)